import numpy as np
import pandas as pd
import glob
import os

dict_practice = {1: 'IneqEq0', 2: 'IneqEq0'}

#You need to text files that have a list of the conditions each trial corresponds to
dict_setA = {}
with open("Dictionaries/trans_setA_list.txt", 'r') as setA_list:
    for line in setA_list:
        (key, val) = line.split()
        dict_setA[int (key)] = val
setA_list.close()

dict_setB = {}
with open("Dictionaries/trans_setB_list.txt", 'r') as setB_list:
    for line in setB_list:
        (key, val) = line.split()
        dict_setB[int (key)] = val
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

### Create dataframe pd from behavioral data
df = pd.DataFrame()

#Reads all the _behavioral files in the folder specified
for f in glob.glob("TransInf_Behav/*behavioralout.txt"):
    filename = os.path.basename(f)
    filename_parts = filename.split('_')
    if filename_parts[2] == 'practice':
        subject = filename_parts[0][:5]+filename_parts[2]
    else:
        subject = filename_parts[0][:5] + filename_parts[2][-1]
    block = filename_parts[2]
    group = filename_parts[0][:2]

    print "processing subject:", subject #, block

    with open(f, 'r') as csvfile:

        dfTemp = pd.read_csv(csvfile, delimiter='\t', header=None, names=['Trial', 'Infer', 'CorrectAnswer',
                                                                          'SubjectResponse', 'ProbRel', 'RT', 'RT_Unc'])

        if len(dfTemp) == 0:
            continue

        dfTemp.insert(0, 'PID', subject)
        dfTemp.insert(1, 'Group', group)
        dfTemp.insert(2, 'Block', block)
        dfTemp['Accuracy'] = np.where(dfTemp['CorrectAnswer'] == dfTemp['SubjectResponse'], 1, 0)

        dfNewCol = dfTemp.apply(map_trial_to_condition, axis=1)
        dfTemp.insert(3, 'Condition', dfNewCol)

        df = df.append(dfTemp, ignore_index=True)

df = df.sort(['PID', 'Trial'])
df = df.reset_index()
df = df.drop('index', axis=1)

### Create dataframe gaze_stats from gaze data
gaze_stats = pd.read_csv('Gaze_Stats/RPPtransinf_gaze_statistics.txt', delimiter='\t', header=None)
gaze_stats.columns = ['PID', 'Comments', 'Trial', 'ConditionNumber','Duration','Fix/SaccadeRatio','TimeToTarget',
                      'FixationsInTarget', 'TotalFixTimeInTarget','TimeToNontarget', 'FixationsInNontarget',
                      'TotalFixTimeInNontarget', 'FixationsInQuestion','TotalFixTimeInQuestion','extra']


gaze_stats = gaze_stats.dropna(how='all')   # Ogama adds an empty column and row to the end
gaze_stats = gaze_stats.dropna(axis=1,how='all')
gaze_stats = gaze_stats.drop(gaze_stats.index[0])   # these are the Ogama labels, which are really long
gaze_stats = gaze_stats.reset_index()
gaze_stats['Trial'] = gaze_stats['Trial'].astype(int)

### Create dataframe new_df with all data
new_df = df.merge(gaze_stats, how='outer', sort=False)
column_order = ['PID', 'Comments', 'Block', 'Trial', 'Condition', 'Infer', 'CorrectAnswer', 'SubjectResponse',
                'Accuracy', 'ProbRel', 'RT', 'RT_Unc', 'Duration', 'Fix/SaccadeRatio', 'TimeToTarget',
                'FixationsInTarget', 'TotalFixTimeInTarget', 'TimeToNontarget', 'FixationsInNontarget',
                'TotalFixTimeInNontarget', 'FixationsInQuestion', 'TotalFixTimeInQuestion']
new_df = new_df[column_order]

#remove block name from PID
for i in range(len(new_df['PID'])):
    new_df['PID'][i] = new_df['PID'][i][0:5]

#allow for different sequence for rt101
rt101_conditions = ['IneqEq2', 'IneqEq1', 'IneqIneq1', 'IneqEq2', 'IneqIneq1', 'IneqIneq2', 'IneqIneq0', 'IneqIneq1',
                    'IneqIneq0', 'IneqEq0', 'IneqEq1', 'IneqEq0', 'IneqIneq0', 'IneqEq2', 'IneqEq2', 'IneqIneq2',
                    'IneqEq2', 'IneqIneq0', 'IneqIneq0', 'IneqIneq2', 'IneqIneq2', 'IneqEq1', 'IneqIneq1', 'IneqEq0',
                    'IneqEq0', 'IneqIneq2', 'IneqEq0', 'IneqEq0', 'IneqIneq0', 'IneqIneq2', 'IneqEq2', 'IneqEq2',
                    'IneqIneq1', 'IneqEq1', 'IneqEq1', 'IneqIneq2', 'IneqEq1', 'IneqIneq1', 'IneqEq2', 'IneqIneq2',
                    'IneqEq1', 'IneqIneq1', 'IneqEq2', 'IneqIneq0', 'IneqEq0', 'IneqIneq2', 'IneqEq1', 'IneqIneq0',
                    'IneqIneq2', 'IneqEq1', 'IneqIneq1', 'IneqEq2', 'IneqEq1', 'IneqEq0', 'IneqEq0', 'IneqIneq1',
                    'IneqIneq0', 'IneqIneq0', 'IneqEq0', 'IneqIneq1']
if new_df['PID'][0] == 'rt101':
    new_df['Condition'][0:60] = rt101_conditions

new_df.to_csv('All_Stats/RPPtransinf_behavioral_gaze_statistics.csv')
