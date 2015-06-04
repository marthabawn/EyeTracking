import pandas as pd
from scipy import stats

### Runs paired t-tests for both tasks on Accuracy and RT

transinfLSAT1 = pd.read_csv('All_Stats/LSAT_T1transinf_behav_gaze_trans.csv')
transinfLSAT2 = pd.read_csv('All_Stats/LSAT_T2transinf_behav_gaze_trans.csv')

matricesLSAT1 = pd.read_csv('All_Stats/LSAT_T1matrices_behav_gaze_trans.csv')
matricesLSAT2 = pd.read_csv('All_Stats/LSAT_T2matrices_behav_gaze_trans.csv')


#TRANSINF

df1 = transinfLSAT1
df2 = transinfLSAT2


df1 = df1[df1['Trial'] < 31]
df1 = df1[df1['Block'] != 'practice']
df1 = df1[df1['Dropped_Out'] == 'no']
df1 = df1[df1['Time2_collected'] == 'yes']

df2 = df2[df2['Trial'] < 31]
df2 = df2[df2['Block'] != 'practice']
df2 = df2[df2['Dropped_Out'] == 'no']
df2 = df2[df2['Time2_collected'] == 'yes']

subj_means1 = df1.groupby('PID').mean()
subj_means2 = df2.groupby('PID').mean()

print 'Transinf Accuracy overall:', stats.ttest_rel(subj_means1['Accuracy'], subj_means2['Accuracy'])

df1_lg = df1[df1['Training'] == 'LG']
df2_lg = df2[df2['Training'] == 'LG']

subj_means1 = df1_lg.groupby('PID').mean()
subj_means2 = df2_lg.groupby('PID').mean()

print 'Transinf Accuracy LG training:', stats.ttest_rel(subj_means1['Accuracy'], subj_means2['Accuracy'])

df1_rc = df1[df1['Training'] == 'RC']
df2_rc = df2[df2['Training'] == 'RC']

subj_means1 = df1_rc.groupby('PID').mean()
subj_means2 = df2_rc.groupby('PID').mean()

print 'Transinf Accuracy RC training:', stats.ttest_rel(subj_means1['Accuracy'], subj_means2['Accuracy'])



df1 = df1[df1['Accuracy'] == 1]
df2 = df2[df2['Accuracy'] == 1]

subj_means1 = df1.groupby('PID').mean()
subj_means2 = df2.groupby('PID').mean()

print 'Transinf RT overall:', stats.ttest_rel(subj_means1['RT'], subj_means2['RT'])

df1_lg = df1[df1['Training'] == 'LG']
df2_lg = df2[df2['Training'] == 'LG']

subj_means1 = df1_lg.groupby('PID').mean()
subj_means2 = df2_lg.groupby('PID').mean()

print 'Transinf RT LG training:', stats.ttest_rel(subj_means1['RT'], subj_means2['RT'])

df1_rc = df1[df1['Training'] == 'RC']
df2_rc = df2[df2['Training'] == 'RC']

subj_means1 = df1_rc.groupby('PID').mean()
subj_means2 = df2_rc.groupby('PID').mean()

print 'Transinf RT RC training:', stats.ttest_rel(subj_means1['RT'], subj_means2['RT'])


#MATRICES

df1 = matricesLSAT1
df2 = matricesLSAT2


df1 = df1[df1['Trial'] < 31]
df1 = df1[df1['Block'] != 'practice']
df1 = df1[df1['Dropped_Out'] == 'no']
df1 = df1[df1['Time2_collected'] == 'yes']

df2 = df2[df2['Trial'] < 31]
df2 = df2[df2['Block'] != 'practice']
df2 = df2[df2['Dropped_Out'] == 'no']
df2 = df2[df2['Time2_collected'] == 'yes']

subj_means1 = df1.groupby('PID').mean()
subj_means2 = df2.groupby('PID').mean()

print 'Matrices Accuracy overall:', stats.ttest_rel(subj_means1['Accuracy'], subj_means2['Accuracy'])

df1_lg = df1[df1['Training'] == 'LG']
df2_lg = df2[df2['Training'] == 'LG']

subj_means1 = df1_lg.groupby('PID').mean()
subj_means2 = df2_lg.groupby('PID').mean()

print 'Matrices Accuracy LG training:', stats.ttest_rel(subj_means1['Accuracy'], subj_means2['Accuracy'])

df1_rc = df1[df1['Training'] == 'RC']
df2_rc = df2[df2['Training'] == 'RC']

subj_means1 = df1_rc.groupby('PID').mean()
subj_means2 = df2_rc.groupby('PID').mean()

print 'Matrices Accuracy RC training:', stats.ttest_rel(subj_means1['Accuracy'], subj_means2['Accuracy'])



df1 = df1[df1['Accuracy'] == 1]
df2 = df2[df2['Accuracy'] == 1]

subj_means1 = df1.groupby('PID').mean()
subj_means2 = df2.groupby('PID').mean()

print 'Matrices RT overall:', stats.ttest_rel(subj_means1['RT_Solving'], subj_means2['RT_Solving'])

df1_lg = df1[df1['Training'] == 'LG']
df2_lg = df2[df2['Training'] == 'LG']

subj_means1 = df1_lg.groupby('PID').mean()
subj_means2 = df2_lg.groupby('PID').mean()

print 'Matrices RT LG training:', stats.ttest_rel(subj_means1['RT_Solving'], subj_means2['RT_Solving'])

df1_rc = df1[df1['Training'] == 'RC']
df2_rc = df2[df2['Training'] == 'RC']

subj_means1 = df1_rc.groupby('PID').mean()
subj_means2 = df2_rc.groupby('PID').mean()

print 'Matrices RT RC training:', stats.ttest_rel(subj_means1['RT_Solving'], subj_means2['RT_Solving'])
