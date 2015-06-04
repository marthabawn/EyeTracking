import pandas as pd
import glob
import os
from collections import Counter

### Counts transitions based on fixation info, creates new fixations file to be used in fixation plots
### May want to rewrite the transition part, using the new fixations file instead of the gazedata_aois files so that we
    # don't count fixations that are too short

# What file to write onto
df = pd.read_csv('All_Stats/LSAT_T1matrices_behavioral_gaze_statistics.csv')
add_df = pd.DataFrame(index=df.index,
                      columns=['Nowhere-Nowhere', 'Nowhere-Problem', 'Nowhere-Answers', 'Problem-Nowhere',
                               'Problem-Problem', 'Problem-Answers', 'Answers-Nowhere', 'Answers-Problem',
                               'Answers-Answers'])

df = pd.concat([df, add_df], axis=1)
df['Trial'] = df['Trial'].astype(int)

fix_details = pd.DataFrame()


#where to get the files with AOI and fixation info
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Matrices\LSAT_T1\Data_with_AOIs'


for f in glob.glob(filepath + '\*gazedata_aois.csv'):
    filename = os.path.basename(f)
    filename_parts = filename.split('_')
    subject = filename_parts[0][0:5]
    block = filename_parts[0][5:]

    print "processing subject:", subject, block

    with open(f, 'r') as csvfile:
        df_old = pd.read_csv(csvfile)

        # uses aois file to define transitions and add them to a list
        fix = []
        transitions = []
        trial_trans = {}
        aoi1 = 'placeholder1'
        aoi2 = 'placeholder2'
        n = 0
        for i in range(1, len(df_old.index)):
            if df_old['Fixation'].iloc[i] != 9999 and df_old['Fixation'].iloc[i] == df_old['Fixation'].iloc[i-1]:
                fix.append(df_old['AOI_Group'].iloc[i])
            else:
                if df_old['Fixation'].iloc[i-1] != 9999:
                    transitions.append((aoi1, aoi2))
                    if len(fix) != 0:
                        aoi1 = aoi2
                        aoi2 = Counter(fix).most_common()[0][0]
                        fix = []

            #add transitions to dictionary at the end of each trial
            if df_old['Trial_Index'].iloc[i] != df_old['Trial_Index'].iloc[i-1] or i == len(df_old.index)-1:
                transitions.append((aoi1, aoi2))
                trial_trans[df_old['Trial_Index'].iloc[i-1]] = transitions[2:]
                fix = []
                transitions = []
                aoi1 = 'placeholder1'
                aoi2 = 'placeholder2'

        print trial_trans
        # counts each kind of transition and records it in the file
        for i in range(len(df.index)):
            try:
                if df['PID'].iloc[i] == subject and block in df['Block'].iloc[i]:
                    df['Nowhere-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'nowhere')]
                    df['Nowhere-Problem'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Problem')]
                    df['Nowhere-Answers'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Answers')]

                    df['Problem-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Problem', 'nowhere')]
                    df['Problem-Problem'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Problem', 'Problem')]
                    df['Problem-Answers'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Problem', 'Answers')]

                    df['Answers-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Answers', 'nowhere')]
                    df['Answers-Problem'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Answers', 'Problem')]
                    df['Answers-Answers'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Answers', 'Answers')]
            except:
                print df['Trial'].iloc[i], ' not found'

        #create dataframe describing each fixation (to be used to make fixation plots)
        df_old = df_old[df_old['Fixation'] != 9999]
        df_copy = df[df['PID'] == subject]
        if block in ['A', 'B']:
            block_copy = 'set' + block
        df_copy = df_copy[df_copy['Block'] == block_copy]

        try:
            for i in range(1, max(df_old['Fixation']) + 1):
                df_old_copy = df_old[df_old['Fixation'] == i]

                trial = Counter(df_old_copy['Trial_Index']).most_common()[0][0]
                cond = df_copy[df_copy['Trial'] == trial]['Condition'].iloc[0]
                aoi = Counter(df_old_copy['AOI']).most_common()[0][0]
                rules_broken = Counter(df_old_copy['AOI_Rules_Broken']).most_common()[0][0]
                if aoi == 'nowhere':
                    if Counter(df_old_copy['AOI_Group']).most_common()[0][0] == 'Problem':
                        aoi = 'nowhere/Problem'
                    elif Counter(df_old_copy['AOI_Group']).most_common()[0][0] == 'Answers':
                        aoi = 'nowhere/Answers'

                fix_details = fix_details.append(pd.DataFrame([subject, block+str(trial), cond, i, aoi,
                                                               max(df_old_copy['Time'])-min(df_old_copy['Time']), rules_broken]).transpose())
        except ValueError:
            print subject+block + ' not found'


fix_details.columns = ['PID', 'Trial', 'Condition', 'Fixation_Num', 'Fixation_AOI', 'Fixation_Dur', 'AOI_Rules_Broken']
fix_details = fix_details[fix_details['Fixation_Dur'] >= 100]



# Add training info (only updated for up to 116)
df.insert(31, 'Training', 'LG')
df.insert(32, 'Dropped_Out', 'no')
df.insert(33, 'Time2_collected', 'no')

for i in df.index:
    if df['PID'].iloc[i][3:] in ['01', '04', '05', '16']:
        df['Dropped_Out'].iloc[i] = 'yes'
    if df['PID'].iloc[i][3:] in ['04', '05', '06', '08', '09', '12', '14']:
        df['Training'].iloc[i] = 'RC'
    # update when new Time2 data comes in - list should contain all subjects for whom we have Time2 data
    if df['PID'].iloc[i][3:] in ['02', '03', '06', '07', '09', '10', '13', '15']:
        df['Time2_collected'].iloc[i] = 'yes'

# save the new version of the file
df.to_csv('All_Stats/LSAT_T1matrices_behav_gaze_trans.csv')
# save the new fixation file
fix_details.to_csv('All_Stats/LSAT_T1matrices_fixations.csv')
