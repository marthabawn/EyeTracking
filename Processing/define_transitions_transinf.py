import pandas as pd
import glob
import os
from collections import Counter

### Counts transitions based on fixation info, creates new fixations file to be used in fixation plots
### May want to rewrite the transition part, using the new fixations file instead of the gazedata_aois files so that we
    # don't count fixations that are too short

# What file to write onto
df = pd.read_csv('All_Stats/LSAT_T1transinf_behavioral_gaze_statistics.csv')
add_df = pd.DataFrame(index=df.index,
                      columns=['Nowhere-Nowhere', 'Nowhere-Q', 'Nowhere-Rel1', 'Nowhere-Rel2', 'Nowhere-Irrel1',
                               'Nowhere-Irrel2', 'Q-Nowhere', 'Q-Q', 'Q-Rel1', 'Q-Rel2', 'Q-Irrel1', 'Q-Irrel2',
                               'Rel1-Nowhere', 'Rel1-Q', 'Rel1-Rel1', 'Rel1-Rel2', 'Rel1-Irrel1', 'Rel1-Irrel2',
                               'Rel2-Nowhere', 'Rel2-Q', 'Rel2-Rel1', 'Rel2-Rel2', 'Rel2-Irrel1', 'Rel2-Irrel2',
                               'Irrel1-Nowhere', 'Irrel1-Q', 'Irrel1-Rel1', 'Irrel1-Rel2', 'Irrel1-Irrel1',
                               'Irrel1-Irrel2', 'Irrel2-Nowhere', 'Irrel2-Q', 'Irrel2-Rel1', 'Irrel2-Rel2',
                               'Irrel2-Irrel1', 'Irrel2-Irrel2'])

df = pd.concat([df, add_df], axis=1)
df['Trial'] = df['Trial'].astype(int)
df = df[df['Trial'] != 31]

fix_details = pd.DataFrame()


# where to get the files with AOI and fixation info
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Transinf\LSAT_T1\Data_with_AOIs'


for f in glob.glob(filepath + '\*gazedata_aois.csv'):
    filename = os.path.basename(f)
    filename_parts = filename.split('_')
    subject = filename_parts[0][:5]
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
                fix.append(df_old['AOI'].iloc[i])
            else:
                if df_old['Fixation'].iloc[i-1] != 9999:
                    transitions.append((aoi1, aoi2))
                    if len(fix) != 0:
                        aoi1 = aoi2
                        aoi2 = Counter(fix).most_common()[0][0]
                        fix = []

            # add transitions to dictionary at the end of each trial
            if df_old['Trial_Num'].iloc[i] != df_old['Trial_Num'].iloc[i-1] or i == len(df_old.index)-1:
                transitions.append((aoi1, aoi2))
                trial_trans[df_old['Trial_Num'].iloc[i-1]] = transitions[2:]
                fix = []
                transitions = []
                aoi1 = 'placeholder1'
                aoi2 = 'placeholder2'


        print trial_trans
        # counts each kind of transition and records it in the file
        for i in range(len(df.index)):
            try:
                if df['PID'].iloc[i][2:] == subject[2:] and block in df['Block'].iloc[i]:
                    df['Nowhere-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'nowhere')]
                    df['Nowhere-Q'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Q')]
                    df['Nowhere-Rel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Rel1')]
                    df['Nowhere-Rel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Rel2')]
                    df['Nowhere-Irrel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Irrel1')]
                    df['Nowhere-Irrel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Irrel2')]

                    df['Q-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Q', 'nowhere')]
                    df['Q-Q'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Q', 'Q')]
                    df['Q-Rel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Q', 'Rel1')]
                    df['Q-Rel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Q', 'Rel2')]
                    df['Q-Irrel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Q', 'Irrel1')]
                    df['Q-Irrel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Q', 'Irrel2')]

                    df['Rel1-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel1', 'nowhere')]
                    df['Rel1-Q'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel1', 'Q')]
                    df['Rel1-Rel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel1', 'Rel1')]
                    df['Rel1-Rel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel1', 'Rel2')]
                    df['Rel1-Irrel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel1', 'Irrel1')]
                    df['Rel1-Irrel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel1', 'Irrel2')]

                    df['Rel2-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel2', 'nowhere')]
                    df['Rel2-Q'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel2', 'Q')]
                    df['Rel2-Rel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel2', 'Rel1')]
                    df['Rel2-Rel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel2', 'Rel2')]
                    df['Rel2-Irrel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel2', 'Irrel1')]
                    df['Rel2-Irrel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Rel2', 'Irrel2')]

                    df['Irrel1-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel1', 'nowhere')]
                    df['Irrel1-Q'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel1', 'Q')]
                    df['Irrel1-Rel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel1', 'Rel1')]
                    df['Irrel1-Rel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel1', 'Rel2')]
                    df['Irrel1-Irrel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel1', 'Irrel1')]
                    df['Irrel1-Irrel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel1', 'Irrel2')]

                    df['Irrel2-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel2', 'nowhere')]
                    df['Irrel2-Q'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel2', 'Q')]
                    df['Irrel2-Rel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel2', 'Rel1')]
                    df['Irrel2-Rel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel2', 'Rel2')]
                    df['Irrel2-Irrel1'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel2', 'Irrel1')]
                    df['Irrel2-Irrel2'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Irrel2', 'Irrel2')]
            except:
                print df['Trial'].iloc[i], ' not found'

        # create dataframe describing each fixation (to be used to make fixation plots)
        df_old = df_old[df_old['Fixation'] != 9999]
        try:
            for i in range(1, max(df_old['Fixation']) + 1):
                df_old_copy = df_old[df_old['Fixation'] == i]

                trial = Counter(df_old_copy['Trial_Num']).most_common()[0][0]
                aoi = Counter(df_old_copy['AOI']).most_common()[0][0]

                fix_details = fix_details.append(pd.DataFrame([subject, block, trial, i, aoi, max(df_old_copy['Time'])-min(df_old_copy['Time'])]).transpose())
        except ValueError:
            print subject+block + ' not found'

fix_details.columns = ['PID', 'Block', 'Trial', 'Fixation_Num', 'Fixation_AOI', 'Fixation_Dur']
fix_details = fix_details[fix_details['Fixation_Dur'] >= 100]


# Add training info (onlu updated for up to 116)
df.insert(60, 'Training', 'RC')
df.insert(61, 'Dropped_Out', 'no')
df.insert(62, 'Time2_collected', 'no')

for i in df.index:
    if df['PID'].iloc[i][3:] in ['01', '04', '05', '16']:
        df['Dropped_Out'].iloc[i] = 'yes'
    if df['PID'].iloc[i][3:] in ['01', '02', '03', '07', '10', '11', '13', '15', '16']:
        df['Training'].iloc[i] = 'LG'
    # update when new Time2 data comes in - list should contain all subjects for whom we have Time2 data
    if df['PID'].iloc[i][3:] in ['02', '03', '06', '07', '09', '10', '13', '15']:
        df['Time2_collected'].iloc[i] = 'yes'

# save the new version of the file
df.to_csv('All_Stats/LSAT_T1transinf_behav_gaze_trans.csv')
# save the new fixation file
fix_details.to_csv('All_Stats/LSAT_T1transinf_fixations.csv')
