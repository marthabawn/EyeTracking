import pandas as pd
import glob
import os
from collections import Counter

df = pd.read_csv('All_Stats/LSAT_T1transinf_behavioral_gaze_statistics1-16.csv')
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

fixs = pd.DataFrame()


#where to get the files with AOI and fixation info
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Transinf\LSAT_T1\Data_with_AOIs'


for f in glob.glob(filepath + '\*gazedata_aois.csv'):
    filename = os.path.basename(f)
    filename_parts = filename.split('_')
    subject = filename_parts[0][:5]
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
            if df_old['Fixation'].iloc[i] == 1 and df_old['Trial_Num'].iloc[i] == df_old['Trial_Num'].iloc[i-1]:
                fix.append(df_old['AOI'].iloc[i])
            else:
                if df_old['Fixation'].iloc[i-1] == 1:
                    fixs = fixs.append(pd.DataFrame([subject, block, df_old['Trial_Num'].iloc[i-1], n, df_old['Time'].iloc[i-1], aoi1]).transpose())
                    transitions.append((aoi1, aoi2))
                    if len(fix) != 0:
                        aoi1 = aoi2
                        aoi2 = Counter(fix).most_common()[0][0]
                        fix = []
                if df_old['Trial_Num'].iloc[i] != df_old['Trial_Num'].iloc[i-1] or i == len(df_old.index)-1:
                    fixs = fixs.append(pd.DataFrame([subject, block, df_old['Trial_Num'].iloc[i-1], n, df_old['Time'].iloc[i-1], aoi1]).transpose())
                    transitions.append((aoi1, aoi2))
                    trial_trans[df_old['Trial_Num'].iloc[i-1]] = transitions[2:]
                    fix = []
                    transitions = []
                    aoi1 = 'nowhere'
                    aoi2 = ''


        print trial_trans
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
            except KeyError:
                print df['Trial'].iloc[i], ' not found'

#fix.columns = ['PID', 'Block', 'Trial', 'FixNumber', 'FixEndTime', 'AOI']

df.to_csv('All_Stats/LSAT_T1transinf_behav_gaze_trans1-16.csv')
#fixs.to_csv('All_Stats/LSAT_T1transinf_fixations.csv')

