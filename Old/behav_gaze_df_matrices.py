import numpy as np
import pandas as pd
import glob
import os

dict_practice = {1: '1', 2: '1'}

dict_setA = {}
with open("Dictionaries/matrix_setA_list.txt", 'r') as setA_list:
    for line in setA_list:
        (key, val) = line.split()
        dict_setA[int (key)] = val
setA_list.close()

dict_setB = {}
with open("Dictionaries/matrix_setB_list.txt", 'r') as setB_list:
    for line in setB_list:
        (key, val) = line.split()
        dict_setB[int(key)] = val
setB_list.close()


def map_trial_to_condition(row):
    if row[2] == 'practice':
        if row[3] in dict_practice:
            return dict_practice[row[3]]
    elif row[2] == 'setA':
        if row[3] in dict_setA:
            return dict_setA[row[3]]
    elif row[2] == 'setB':
        if row[3] in dict_setB:
            return dict_setB[row[3]]


    return 'N/A'

dfm = pd.DataFrame()

#It's easier to separete the files from subject 1-10 into a separate folder
for f in glob.glob("Matrices_Behav_Data/LSAT_T1/*behavioralout.txt"):
    filename = os.path.basename(f)
    filename_parts = filename.split('_')
    if filename_parts[2] == 'practice':
        subject = filename_parts[0][:5]+filename_parts[2]
    else:
        subject = filename_parts[0][:5] + filename_parts[2][-1]
    block = filename_parts[2]
    group = filename_parts[0][:2]

    print "processing subject:", subject

    with open(f, 'r') as csvfile:

        dfTemp = pd.read_csv(csvfile, delimiter='\t', header=None,
                             names=['Trial', 'CorrectAnswer', 'SolutionClicked', 'SubjectResponse', 'RT_Solving',
                                    'RT_SolvingUnc', 'RT_Response', 'RT_ResponseUnc', 'OrderSolutions'])

        if len(dfTemp) == 0:
            continue

        dfTemp.insert(0, 'PID', subject)
        dfTemp.insert(1, 'Group', group)
        dfTemp.insert(2, 'Block', block)
        dfTemp['Accuracy'] = np.where(dfTemp['CorrectAnswer'] == dfTemp['SubjectResponse'], 1, 0)

        dfNewCol = dfTemp.apply(map_trial_to_condition, axis=1)
        dfTemp.insert(3, 'Condition', dfNewCol)

        dfm = dfm.append(dfTemp, ignore_index=True)

dfm = dfm.sort(['PID', 'Trial'])
dfm = dfm.reset_index()
dfm = dfm.drop('index', axis=1)

### Create dataframe gaze_stats from gaze data
gaze_stats = pd.read_csv('Gaze_Stats/LSAT_T1matrices_gaze_statistics.txt', delimiter='\t', header=None)
gaze_stats.columns = ['PID', 'Comments', 'Trial', 'Duration', 'Fix/SaccadeRatio',
                      'FixationsInProblem', 'TimeToProblem', 'TotalFixTimeInProblem', 'FixationsInAnswers',
                      'TimeToAnswers', 'TotalFixTimeInAnswers', 'Ones', 'extra']

gaze_stats = gaze_stats.dropna(how='all')   # Ogama adds an empty column and row to the end
gaze_stats = gaze_stats.dropna(axis=1, how='all')
gaze_stats = gaze_stats.drop('Ones', axis=1)
gaze_stats = gaze_stats.drop(gaze_stats.index[0])   # these are the Ogama labels, which are really long
gaze_stats = gaze_stats.reset_index()
gaze_stats['Trial'] = gaze_stats['Trial'].astype(int)

### Create dataframe new_df with all data
new_df = dfm.merge(gaze_stats, how='outer', sort=False)
column_order = ['PID', 'Comments', 'Block', 'Trial', 'Condition', 'CorrectAnswer', 'SolutionClicked', 'SubjectResponse',
                'Accuracy', 'RT_Solving', 'RT_SolvingUnc', 'RT_Response', 'RT_ResponseUnc', 'OrderSolutions',
                'Duration', 'Fix/SaccadeRatio', 'FixationsInProblem', 'TimeToProblem', 'TotalFixTimeInProblem',
                'FixationsInAnswers', 'TimeToAnswers', 'TotalFixTimeInAnswers']
new_df = new_df[column_order]

#remove block name from PID
for i in range(len(new_df['PID'])):
    new_df['PID'][i] = new_df['PID'][i][0:5]

new_df.to_csv('All_Stats/LSAT_T1matrices_behavioral_gaze_statistics.csv')
