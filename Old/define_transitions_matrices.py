import pandas as pd
import glob
import os
from collections import Counter

df = pd.read_csv('All_Stats/LSAT_T1matrices_behavioral_gaze_statistics.csv')
add_df = pd.DataFrame(index=df.index,
                      columns=['Nowhere-Nowhere', 'Nowhere-Problem', 'Nowhere-Answers', 'Problem-Nowhere',
                               'Problem-Problem', 'Problem-Answers', 'Answers-Nowhere', 'Answers-Problem',
                               'Answers-Answers'])

df = pd.concat([df, add_df], axis=1)
df['Trial'] = df['Trial'].astype(int)

fixs = pd.DataFrame()


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

        fix = []
        transitions = []
        trial_trans = {}
        aoi1 = 'nowhere'
        aoi2 = ''
        n = 0
        for i in range(1, len(df_old.index)):
            if df_old['Fixation'].iloc[i] == 1 and df_old['Trial_Index'].iloc[i] == df_old['Trial_Index'].iloc[i-1]:
                fix.append(df_old['AOI'].iloc[i])
            else:
                if df_old['Fixation'].iloc[i-1] == 1:
                    fixs = fixs.append(pd.DataFrame([subject, block, df_old['Trial_Index'].iloc[i-1], n, df_old['Time'].iloc[i-1], aoi1]).transpose())
                    transitions.append((aoi1, aoi2))
                    if len(fix) != 0:
                        aoi1 = aoi2
                        aoi2 = Counter(fix).most_common()[0][0]
                        fix = []
                if df_old['Trial_Index'].iloc[i] != df_old['Trial_Index'].iloc[i-1] or i == len(df_old.index)-1:
                    fixs = fixs.append(pd.DataFrame([subject, block, df_old['Trial_Index'].iloc[i-1], n, df_old['Time'].iloc[i-1], aoi1]).transpose())
                    transitions.append((aoi1, aoi2))
                    trial_trans[df_old['Trial_Index'].iloc[i-1]] = transitions[2:]
                    fix = []
                    transitions = []
                    aoi1 = 'nowhere'
                    aoi2 = ''


        print trial_trans

        for i in range(len(df.index)):
            try:
                if df['PID'].iloc[i][2:] == subject[2:] and block in df['Block'].iloc[i]:
                    df['Nowhere-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'nowhere')]
                    df['Nowhere-Problem'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Problem')]
                    df['Nowhere-Answers'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('nowhere', 'Answers')]

                    df['Problem-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Problem', 'nowhere')]
                    df['Problem-Problem'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Problem', 'Problem')]
                    df['Problem-Answers'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Problem', 'Answers')]

                    df['Answers-Nowhere'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Answers', 'nowhere')]
                    df['Answers-Problem'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Answers', 'Problem')]
                    df['Answers-Answers'].iloc[i] = Counter(trial_trans[df['Trial'].iloc[i]])[('Answers', 'Answers')]
            except KeyError:
                print df['Trial'].iloc[i], ' not found'

#fix.columns = ['PID', 'Block', 'Trial', 'FixNumber', 'FixEndTime', 'AOI']

df.to_csv('All_Stats/LSAT_T1matrices_behav_gaze_trans.csv')
fixs.to_csv('All_Stats/LSAT_T1matrices_fixations.csv')








