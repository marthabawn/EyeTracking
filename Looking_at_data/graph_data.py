import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

### Creates graphs for both tasks (transinf first, matrices at the bottom)
### Uncomment each section to get the graphs, also uncomment lines to exclude some trials
### Could use some cleaning up
### Some error bars not working. Temporary fix = run the section with a print errors line, then manually define error

matrices1 = pd.read_csv('All_Stats/RPPmatrices_behavioral_gaze_statistics1-9.csv')

matrices2 = pd.read_csv('All_Stats/RPPmatrices_behavioral_gaze_statistics10-22.csv')

transinf = pd.read_csv('All_Stats/RPPtransinf_behavioral_gaze_statistics.csv')

transinfLSAT1 = pd.read_csv('All_Stats/LSAT_T1transinf_behav_gaze_trans.csv')
transinfLSAT2 = pd.read_csv('All_Stats/LSAT_T2transinf_behav_gaze_trans.csv')

matricesLSAT1 = pd.read_csv('All_Stats/LSAT_T1matrices_behav_gaze_trans.csv')
matricesLSAT2 = pd.read_csv('All_Stats/LSAT_T2matrices_behav_gaze_trans.csv')


df1 = matricesLSAT1
df2 = matricesLSAT2

df1.insert(3, 'Session', 1)
df2.insert(3, 'Session', 2)

df = pd.concat([df1, df2])

print df.columns.tolist()

#use this to move around legend
#plt.legend(loc='center', bbox_to_anchor=(1.0, 0.5))

#df = df[df['Trial'] < 31]
#df = df[df['Block'] != 'practice']
#df = df[df['Training'] == 'LG']
#df = df[df['Dropped_Out'] == 'no']
#df = df[df['Time2_collected'] == 'yes']
#df = df[df['Accuracy'] == 1]

###TRANSINF

# print df.groupby(['PID']).mean()[['Accuracy', 'RT']]
# print df.groupby(['Block']).mean()[['Accuracy', 'RT']]
# print df.groupby(['Block'])['RT'].describe()
# print df.groupby(['Condition']).mean()[['Accuracy', 'RT']]
# print df.groupby(['PID', 'Block']).mean()[['Accuracy', 'RT']]
# print df[df['PID'] != 'tp101'].groupby('Block').mean()[['Accuracy', 'RT']]

#print df[df['PID'] != 'tp101'].groupby('PID')['RT'].describe(exclude=['min', '25%', '75%', 'max'])

#df = df[df['Accuracy'] == 1]

# df.boxplot(column='RT', by=['Block', 'Accuracy'])
# plt.title('Response Time by Block and Accuracy')
# plt.show()
#
# means = df.groupby('PID').mean()
# print means[['RT']].describe()
# means.boxplot(column='Accuracy')
# plt.title('Overall Accuracy')
# plt.show()
# means.boxplot(column='RT')
# plt.title('Overall Response Time')
# plt.show()
# means.boxplot(column='RT', by='Accuracy')
# plt.title('Response Time by Average Accuracy')
# plt.show()

# means = df.groupby('Condition').mean()
# errors = df.groupby('Condition')['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='Accuracy', yerr=errors, title='Accuracy by Condition')
# plt.show()
# errors = df.groupby('Condition')['RT'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='RT', yerr=errors, title='Response Time by Condition')
# plt.show()

# means = df.groupby('Block').mean()
# errors = df.groupby('Block').std()['Accuracy']/(len(df.index)**0.5)
# means.plot(yerr=errors, kind='bar', y='Accuracy', title='Accuracy by Block')
# plt.show()
# errors = df.groupby('Block').std()['RT']/(len(df.index)**0.5)
# means.plot(yerr=errors, kind='bar', y='RT', title='Response Time by Block')
# plt.show()

# timeto = df[['PID', 'TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].mean()
# errors = df[['PID', 'TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].std()/(len(df.index)**0.5)
# timeto.plot(yerr=errors, kind='bar', title='Time to First Fixation')
# plt.show()
#
# timeto = df.groupby('Condition')[['PID', 'TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].mean()
# errors = df.groupby('Condition')[['PID', 'TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].std()/(len(df.index)**0.5)
# timeto.plot(yerr=errors, kind='bar', title='Time to First Fixation by Condition')
# plt.show()
#
# timeto = df.groupby('Accuracy')[['PID', 'TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].mean()
# errors = df.groupby('Accuracy')[['PID', 'TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].std()/(len(df.index)**0.5)
# timeto.plot(yerr=errors, kind='bar', title='Time to First Fixation by Accuracy')
# plt.show()

# fixtime = df[['PID', 'TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].mean()
# errors = df[['PID', 'TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].std()/(len(df.index)**0.5)
# fixtime.plot(yerr=errors, kind='bar', title='Total Fixation Time')
# plt.show()
#
# fixtime = df[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum()
# print fixtime
# totaltime = df[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum().sum(axis=1)
# print totaltime
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs')
# plt.show()
#
# fixtime = df.groupby('Condition')[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum()
# print fixtime
# totaltime = df.groupby('Condition')[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum().sum(axis=1)
# print totaltime
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs by Condition')
# plt.show()
#
# fixtime = df.groupby('Condition')[['PID', 'TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].mean()
# errors = df.groupby('Condition')[['PID', 'TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].std()/(len(df.index)**0.5)
# fixtime.plot(yerr=errors, kind='bar', title='Total Fixation Time by Condition')
# plt.legend(loc='center right')
# plt.show()

# fixtime = df.groupby('Accuracy')[['PID', 'TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].mean()
# errors = df.groupby('Accuracy')[['PID', 'TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].std()/(len(df.index)**0.5)
# fixtime.plot(yerr=errors, kind='bar', title='Total Fixation Time by Accuracy')
# plt.show()
#
# fixtime = df.groupby('Accuracy')[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum()
# print fixtime
# totaltime = df.groupby('Accuracy')[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum().sum(axis=1)
# print totaltime
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs by Accuracy')
# plt.show()

# df['Median_RT'] = 0
# for i in df.index:
#     df['Median_RT'][i] = df.groupby('PID')['RT'].median()[df['PID'][i]]
#
# split_rt = df.groupby(df['RT'] > df['Median_RT'])

# timeto = split_rt[['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].mean()
# errors = split_rt[['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget']].std()/(len(df[df['Accuracy'] == 1].index)**0.5)
# timeto.plot(yerr=errors, kind='bar', title='Time to First Fixation with Split Response Time')
# plt.show()
#
# fixtime = split_rt[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].mean()
# errors = split_rt[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].std()/(len(df[df['Accuracy'] == 1].index)**0.5)
# fixtime.plot(yerr=errors, kind='bar', title='Total Fixation Time with Split Response Time')
# plt.show()
#
# fixtime = split_rt[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum()
# print fixtime
# totaltime = split_rt[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum().sum(axis=1)
# print totaltime
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs with Split Response Time')
# plt.show()

# trans = df[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].mean()
# errors = df[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Average Number of Transitions per Trial')
# plt.show()
#
# trans = df.groupby('Condition')[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].mean()
# errors = df.groupby('Condition')[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Average Number of Transitions per Trial by Condition')
# plt.show()
#
# trans = df.groupby('Accuracy')[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].mean()
# errors = df.groupby('Accuracy')[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Average Number of Transitions per Trial by Accuracy')
# plt.show()

# trans = split_rt[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].mean()
# errors = split_rt[['Rel1-Rel1', 'Rel2-Rel2', 'Rel1-Rel2', 'Rel2-Rel1']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Average Number of Transitions with RT Median Split')
# plt.show()


# relation_trans = split_rt[['Rel1-Rel1', 'Rel1-Rel2', 'Rel1-Irrel1', 'Rel1-Irrel2', 'Rel2-Rel1', 'Rel2-Rel2',
#                            'Rel2-Irrel1', 'Rel2-Irrel2', 'Irrel1-Rel1', 'Irrel1-Rel2', 'Irrel1-Irrel1', 'Irrel1-Irrel2',
#                            'Irrel2-Rel1', 'Irrel2-Rel2', 'Irrel2-Irrel1', 'Irrel2-Irrel2']].sum().sum(axis=1)
# print relation_trans
# relevant_trans = split_rt[['Rel1-Rel1', 'Rel1-Rel2', 'Rel2-Rel1', 'Rel2-Rel2']].sum()
# print relevant_trans
# prop = relevant_trans.divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Transitions between Relevant Relations with Split Response Time')
# plt.show()
#
# relation_trans = df[['Rel1-Rel1', 'Rel1-Rel2', 'Rel1-Irrel1', 'Rel1-Irrel2', 'Rel2-Rel1', 'Rel2-Rel2',
#                            'Rel2-Irrel1', 'Rel2-Irrel2', 'Irrel1-Rel1', 'Irrel1-Rel2', 'Irrel1-Irrel1', 'Irrel1-Irrel2',
#                            'Irrel2-Rel1', 'Irrel2-Rel2', 'Irrel2-Irrel1', 'Irrel2-Irrel2']].sum().sum(axis=1)
# print relation_trans
# relevant_trans = df[['Rel1-Rel1', 'Rel1-Rel2', 'Rel2-Rel1', 'Rel2-Rel2']].sum()
# print relevant_trans
# prop = relevant_trans.divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Transitions between Relevant Relations')
# plt.show()

# relation_trans = df.groupby('Accuracy')[['Rel1-Rel1', 'Rel1-Rel2', 'Rel1-Irrel1', 'Rel1-Irrel2', 'Rel2-Rel1', 'Rel2-Rel2',
#                            'Rel2-Irrel1', 'Rel2-Irrel2', 'Irrel1-Rel1', 'Irrel1-Rel2', 'Irrel1-Irrel1', 'Irrel1-Irrel2',
#                            'Irrel2-Rel1', 'Irrel2-Rel2', 'Irrel2-Irrel1', 'Irrel2-Irrel2']].sum().sum(axis=1)
# print relation_trans
# relevant_trans = df.groupby('Accuracy')[['Rel1-Rel1', 'Rel1-Rel2', 'Rel2-Rel1', 'Rel2-Rel2']].sum()
# print relevant_trans
# prop = relevant_trans.divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Transitions between Relevant Relations by Accuracy')
# plt.show()

# df['rel_rel'] = df[['Rel1-Rel1', 'Rel1-Rel2', 'Rel2-Rel1', 'Rel2-Rel2']].sum(axis=1)
# df['irrel_irrel'] = df[['Irrel1-Irrel1', 'Irrel1-Irrel2', 'Irrel2-Irrel1', 'Irrel2-Irrel2']].sum(axis=1)
# df['rel_irrel'] = df[['Rel1-Irrel1', 'Rel1-Irrel2', 'Rel2-Irrel1', 'Rel2-Irrel2']].sum(axis=1)
# df['irrel_rel'] = df[['Irrel1-Rel1', 'Irrel1-Rel2', 'Irrel2-Rel1', 'Irrel2-Rel2']].sum(axis=1)
# df['rel-question'] = df[['Rel1-Q', 'Rel2-Q']].sum(axis=1)
# df['question-rel'] = df[['Q-Rel1', 'Q-Rel2']].sum(axis=1)
# df['irrel-question'] = df[['Irrel1-Q', 'Irrel2-Q']].sum(axis=1)
# df['question-irrel'] = df[['Q-Irrel1', 'Q-Irrel2']].sum(axis=1)

# relation_trans = df[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# prop = df[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions between Relations')
# plt.show()

# relation_trans = df.groupby('Accuracy')[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# prop = df.groupby('Accuracy')[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions between Relations by Accuracy')
# plt.show()

# relation_trans = df.groupby('Condition')[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# prop = df.groupby('Condition')[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions between Relations by Condition')
# plt.show()
#
# relation_trans = df.groupby(df['RT'] > df['Median_RT'])[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# prop = df[df['Accuracy'] == 1].groupby(df['RT'] > df['Median_RT'])[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions between Relations with Split Response Time')
# plt.show()

#df = df[df['Accuracy'] == 1]

## Compare T1 to T2
# groups = df.groupby(['Session', 'PID'])
# means = groups[['Session', 'PID', 'Accuracy', 'RT']].mean()
# print means
# means.boxplot(column='Accuracy', by='Session')
# plt.title('Overall Accuracy')
# plt.ylabel('Percent Correct')
# plt.show()
# means.boxplot(column='RT', by='Session')
# plt.title('Overall Response Time')
# plt.ylabel('Response Time (ms)')
# plt.show()

# groups = df.groupby(['Condition', 'Session'])
# means = groups['Accuracy'].mean()
# errors = groups['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Accuracy by Condition')
# plt.ylabel('Percent Correct')
# plt.show()
# means = groups['RT'].mean()
# errors = groups['RT'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Response Time by Condition')
# plt.ylabel('Response Time (ms)')
# plt.show()

# groups = df.groupby(['Block', 'Session'])
# means = groups['Accuracy'].mean()
# errors = groups['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Accuracy by Block')
# plt.ylabel('Percent Correct')
# plt.show()
# means = groups['RT'].mean()
# errors = groups['RT'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Response Time by Block')
# plt.ylabel('Response Time (ms)')
# plt.show()

######## Fix error bars
# groups = df.groupby(['Session'])
# timeto = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].mean()
# errors = [[41.401180, 51.949465], [27.051721, 24.397744], [35.478374, 32.720886]]
# #errors = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].std()/(len(df.index)**0.5)
# print errors
# ax = timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation in AOI')
# plt.ylabel('Time to First Fixation (ms)')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels, loc='center right')
# plt.show()

# groups = df.groupby(['Session', 'Accuracy'])
# timeto = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].mean()
# errors = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].std()/(len(df.index)**0.5)
# timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation by Accuracy')
# plt.show()

# groups = df.groupby(['Session', df['RT'] > df['Median_RT']])
# timeto = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].mean()
# errors = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].std()/(len(df.index)**0.5)
# ax = timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation with Median Split')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels, loc='upper center')
# plt.ylabel('Time to First Fixation (ms)')
# plt.show()

######## Fix error bars
# groups = df.groupby('Session')
# fixtime = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].mean()
# errors = [[28.990580, 29.817727], [106.507361, 97.770238], [40.832301, 39.916786]]
# #errors = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].std()/(len(df.index)**0.5)
# ax = fixtime.plot(kind='bar', yerr=errors, title='Total Fixation Time in AOI')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels, loc='center right')
# plt.ylabel('Time Fixated in AOI (ms)')
# plt.show()

# groups = df.groupby(['Session', 'Accuracy'])
# fixtime = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].mean()
# errors = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].std()/(len(df.index)**0.5)
# fixtime.plot(kind='bar', yerr=errors, title='Total Fixation Time by Accuracy')
# plt.show()

# groups = df.groupby(['Session', df['RT'] > df['Median_RT']])
# timeto = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].mean()
# errors = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].std()/(len(df.index)**0.5)
# ax = timeto.plot(kind='bar', yerr=errors, title='Total Fixation Time in AOI with Median Split')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels)
# plt.ylabel('Time Fixated in AOI (ms)')
# plt.show()
#
######## Fix error bars
# groups = df.groupby('Session')
# trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].mean()
# errors = [[0.195413, 0.148735], [0.060991, 0.041921], [0.056441, 0.045457], [0.061702, 0.048195]]
# #errors = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].std()/(len(df.index)**0.5)
# print errors
# trans.plot(kind='bar', yerr=errors, title='Number of Transitions')
# plt.ylabel('Number of Transitions per Trial')
# plt.show()

# groups = df.groupby(['Session', 'Accuracy'])
# trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].mean()
# errors = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions by Accuracy')
# plt.show()

# groups = df.groupby(['Session', df['RT'] > df['Median_RT']])
# trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].mean()
# errors = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions with Median Split')
# plt.ylabel('Transitions per Trial')
# plt.legend(loc='upper center')
# plt.show()

####### Fix error bars
# groups = df.groupby('Session')
# trans = groups[['rel-question', 'question-rel', 'irrel-question', 'question-irrel']].mean()
# errors = [[0.079224, 0.062992], [0.072689, 0.055706], [0.034098, 0.028251], [0.033281, 0.027732]]
# #errors = groups[['rel-question', 'question-rel', 'irrel-question', 'question-irrel']].std()/(len(df.index)**0.5)
# print errors
# trans.plot(kind='bar', yerr=errors, title='Number of Transitions To/From Question')
# plt.ylabel('Number of Transitions per Trial')
# plt.show()
#
######## Fix error bars
# groups = df.groupby('Session')
# trans = groups[['rel-question', 'question-rel']].mean()
# errors = [[0.079224, 0.062992], [0.072689, 0.055706]]
# #errors = groups[['rel-question', 'question-rel']].std()/(len(df.index)**0.5)
# print errors
# trans.plot(kind='bar', yerr=errors, title='Number of Transitions Between Question and Relevant Relations')
# plt.ylabel('Number of Transitions per Trial')
# plt.show()

# groups = df.groupby('Session')
# fixtime = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].mean()
# errors = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].std()/(len(df.index)**0.5)
# fixtime.plot(kind='bar', title='Total Fixation Time in AOI')
# plt.ylabel('Time Fixated in AOI (ms)')
# plt.show()

# groups = df.groupby('Session')
# fixtime = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].mean()
# errors = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].std()/(len(df.index)**0.5)
# fixtime.plot(kind='bar', title='Total Fixation Time in AOI')
# plt.ylabel('Time Fixated in AOI (ms)')
# plt.show()

# groups = df.groupby('Session')
# fixtime = groups[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum()
# totaltime = groups[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum().sum(axis=1)
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# ax = prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels)
# plt.ylabel('% of Time Fixated in AOIs')
# plt.show()

# groups = df.groupby(['Session', df['RT'] > df['Median_RT']])
# fixtime = groups[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum()
# totaltime = groups[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum().sum(axis=1)
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# ax = prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels, loc='upper center')
# plt.ylabel('% of Time Fixated in AOIs')
# plt.show()
#
# groups = df.groupby('Session')
# relation_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# relevant_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum()
# prop = relevant_trans.divide(relation_trans, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions')
# plt.ylabel('% of Transitions between Relations')
# plt.show()

# groups = df.groupby(['Session', 'Accuracy'])
# relation_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# print relation_trans
# relevant_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum()
# print relevant_trans
# prop = relevant_trans.divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions by Accuracy')
# plt.legend(loc='center right')
# plt.show()

# groups = df.groupby(['Session', df['RT'] > df['Median_RT']])
# relation_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# relevant_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum()
# prop = relevant_trans.divide(relation_trans, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions with Median Split')
# plt.legend(loc='center right')
# plt.ylabel('% of Transitions between Relations')
# plt.show()


# groups = df.groupby(['PID', 'Training'])
# means = groups[['Session', 'Accuracy', 'RT']].mean()
# print means
# means.boxplot(column='Accuracy', by=['Session', 'Training'])
# plt.title('Overall Accuracy')
# plt.show()
# means.boxplot(column='RT', by=['Session', 'Training'])
# plt.title('Overall Response Time')
# plt.show()

# means = df.groupby(['Training', 'Session']).mean()
# errors = df.groupby(['Training', 'Session'])['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='Accuracy', yerr=errors, title='Accuracy by Training')
# plt.show()
# errors = df.groupby(['Training', 'Session'])['RT'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='RT', yerr=errors, title='Response Time by Training')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# timeto = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].mean()
# errors = groups['TimeToQuestion', 'TimeToTarget', 'TimeToNontarget'].std()/(len(df.index)**0.5)
# ax = timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation in AOI by Training')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels)
# plt.ylabel('Time Until First Fixation (ms)')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# timeto = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].mean()
# errors = groups['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget'].std()/(len(df.index)**0.5)
# ax = timeto.plot(kind='bar', yerr=errors, title='Total Time Fixated in AOI by Training')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels)
# plt.ylabel('Time Until First Fixation (ms)')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].mean()
# errors = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions by Training')
# plt.ylabel('Transitions per Trial')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# relation_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum().sum(axis=1)
# relevant_trans = groups[['rel_rel', 'irrel_irrel', 'rel_irrel', 'irrel_rel']].sum()
# prop = relevant_trans.divide(relation_trans, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions by Training')
# plt.ylabel('% of All Transitions between Relations')
# plt.show()

# groups = df.groupby(['Training', 'Session'])
# fixtime = groups[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum()
# totaltime = groups[['TotalFixTimeInQuestion', 'TotalFixTimeInTarget', 'TotalFixTimeInNontarget']].sum().sum(axis=1)
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# ax = prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs by Training')
# bars, labels = ax.get_legend_handles_labels()
# labels = ['Question', 'Relevant', 'Irrelevant']
# plt.legend(bars, labels)
# plt.ylabel('% of Time Fixated in AOIs')
# plt.show()



### MATRICES

# print df.groupby(['PID']).mean()[['Accuracy', 'RT_Solving']]
# print df.groupby(['Block']).mean()[['Accuracy', 'RT_Solving']]
# print df.groupby(['Block'])['RT_Solving'].describe()
# print df.groupby(['Condition']).mean()[['Accuracy', 'RT_Solving']]
# print df.groupby(['PID', 'Block']).mean()[['Accuracy', 'RT_Solving']]

# df = df[df['Block'] != 'practice']
# df = df[df['RT_Solving'] < 140000]  #exclude one outlier trial from subject tp118
# df_copy = df[df['PID'] == 'tp118']
# print df_copy['RT_Solving'].describe()

# df.boxplot(column='RT_Solving', by=['Block', 'Accuracy'])
# plt.title('Response Time by Block and Accuracy')
# plt.show()

# means = df.groupby('PID').mean()
# means.boxplot(column='Accuracy')
# plt.title('Overall Accuracy')
# plt.show()
# means.boxplot(column='RT_Solving')
# plt.title('Overall Response Time')
# plt.show()
# means.boxplot(column='RT_Solving', by='Accuracy')
# plt.title('Response Time by Average Accuracy')
# plt.show()

# means = df.groupby('Condition').mean()
# errors = df.groupby('Condition')['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='Accuracy', yerr=errors, title='Accuracy by Condition')
# plt.show()
# errors = df.groupby('Condition')['RT_Solving'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='RT_Solving', yerr=errors, title='Response Time by Condition')
# plt.show()

# means = df.groupby('Block').mean()
# errors = df.groupby('Block').std()['Accuracy']/(len(df.index)**0.5)
# means.plot(yerr=errors, kind='bar', y='Accuracy', title='Accuracy by Block')
# plt.show()
# errors = df.groupby('Block').std()['RT_Solving']/(len(df.index)**0.5)
# means.plot(yerr=errors, kind='bar', y='RT_Solving', title='Response Time by Block')
# plt.show()

# timeto = df[['PID', 'TimeToProblem', 'TimeToAnswers']].mean()
# errors = df[['PID', 'TimeToProblem', 'TimeToAnswers']].std()/(len(df.index)**0.5)
# timeto.plot(yerr=errors, kind='bar', title='Time to First Fixation')
# plt.show()

# timeto = df.groupby('Condition')[['PID', 'TimeToProblem', 'TimeToAnswers']].mean()
# errors = timeto.std()/(len(timeto.index)**0.5)
# timeto.plot(yerr=errors, kind='bar', title='Time to First Fixation by Condition')
# plt.show()

# timeto = df.groupby('Accuracy')[['PID', 'TimeToProblem', 'TimeToAnswers']].mean()
# errors = df.groupby('Accuracy')[['PID', 'TimeToProblem', 'TimeToAnswers']].std()/(len(df.index)**0.5)
# timeto.plot(yerr=errors, kind='bar', title='Time to First Fixation by Accuracy')
# plt.show()

# fixtime = df[['PID', 'TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].mean()
# errors = df[['PID', 'TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].std()/(len(df.index)**0.5)
# fixtime.plot(yerr=errors, kind='bar', title='Total Fixation Time')
# plt.show()

# fixtime = df.groupby('Condition')[['PID', 'TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].mean()
# errors = df.groupby('Condition')[['PID', 'TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].std()/(len(df.index)**0.5)
# fixtime.plot(yerr=errors, kind='bar', title='Total Fixation Time by Condition')
# plt.show()

# fixtime = df.groupby('Accuracy')[['PID', 'TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].mean()
# errors = df.groupby('Accuracy')[['PID', 'TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].std()/(len(df.index)**0.5)
# fixtime.plot(yerr=errors, kind='bar', title='Total Fixation Time by Accuracy')
# plt.show()

# trans = df[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].mean()
# errors = df[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions')
# plt.show()

# trans = df.groupby('Condition')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].mean()
# errors = df.groupby('Condition')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions by Condition')
# plt.show()

# trans = df.groupby('Accuracy')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].mean()
# print trans
# errors = df.groupby('Accuracy')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].std()/(len(df.index)**0.5)
# print errors
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions by Accuracy')
# plt.show()

# relation_trans = df[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum().sum(axis=1)
# print relation_trans
# relevant_trans = df[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum()
# print relevant_trans
# prop = relevant_trans.divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions')
# plt.show()

# relation_trans = df.groupby('Accuracy')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum().sum(axis=1)
# print relation_trans
# relevant_trans = df.groupby('Accuracy')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum()
# print relevant_trans
# prop = relevant_trans.divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions by Accuracy')
# plt.show()

# relation_trans = df.groupby('Condition')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum().sum(axis=1)
# print relation_trans
# relevant_trans = df.groupby('Condition')[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum()
# print relevant_trans
# prop = relevant_trans.divide(relation_trans, axis='index')
# print prop
# errors = prop.std()/(len(prop.index)**0.5)
# print errors
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions by Condition')
# plt.show()

#COMPARING TIME1 TO TIME2


#df = df[df['Accuracy'] == 1]

# groups = df.groupby(['Session', 'PID'])
# means = groups[['Session', 'PID', 'Accuracy', 'RT_Solving']].mean()
# means.boxplot(column='Accuracy', by='Session')
# plt.title('Overall Accuracy')
# plt.show()
# means.boxplot(column='RT_Solving', by='Session')
# plt.title('Overall Response Time')
# plt.show()

# groups = df.groupby(['Session', 'Condition'])
# means = groups['Accuracy'].mean()
# errors = groups['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Accuracy by Condition')
# plt.ylabel('Percent Correct')
# plt.show()
# means = groups['RT_Solving'].mean()
# errors = groups['RT_Solving'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Response Time by Condition')
# plt.ylabel('Response Time (ms)')
# plt.show()
#
# groups = df.groupby(['Block', 'Session'])
# means = groups['Accuracy'].mean()
# errors = groups['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Accuracy by Block')
# plt.ylabel('Percent Correct')
# plt.show()
# means = groups['RT_Solving'].mean()
# errors = groups['RT_Solving'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', yerr=errors, title='Response Time by Block')
# plt.ylabel('Response Time (ms)')
# plt.show()

######## Fix error bars
# groups = df.groupby('Session')
# timeto = groups['TimeToProblem', 'TimeToAnswers'].mean()
# print timeto
# errors = [[236.821723, 13.809219], [506.598266, 248.797964]]
# #errors = groups['TimeToProblem', 'TimeToAnswers'].std()/(len(df.index)**0.5)
# print errors
# timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation in AOI')
# plt.ylabel('Time Until First Fixation (ms)')
# plt.show()
#
# groups = df.groupby(['Session', 'Condition'])
# timeto = groups['TimeToProblem', 'TimeToAnswers'].mean()
# errors = groups['TimeToProblem', 'TimeToAnswers'].std()/(len(df.index)**0.5)
# timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation in AOI by Condition')
# plt.ylabel('Time Until First Fixation (ms)')
# plt.show()
#
# groups = df.groupby(['Session', 'Accuracy'])
# timeto = groups['TimeToProblem', 'TimeToAnswers'].mean()
# errors = groups['TimeToProblem', 'TimeToAnswers'].std()/(len(df.index)**0.5)
# timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation in AOI by Accuracy')
# plt.ylabel('Time Until First Fixation (ms)')
# plt.show()
#
######## Fix error bars
# groups = df.groupby('Session')
# fixtime = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].mean()
# errors = [[593.385274, 316.825959], [120.339961, 80.494523]]
# #errors = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].std()/(len(df.index)**0.5)
# print errors
# fixtime.plot(kind='bar', yerr=errors, title='Total Fixation Time in AOI')
# plt.ylabel('Fixation Time (ms)')
# plt.show()
#
# groups = df.groupby(['Session', 'Condition'])
# fixtime = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].mean()
# errors = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].std()/(len(df.index)**0.5)
# fixtime.plot(kind='bar', yerr=errors, title='Total Fixation Time in AOI by Condition')
# plt.ylabel('Fixation Time (ms)')
# plt.show()
#
# groups = df.groupby(['Session', 'Accuracy'])
# fixtime = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].mean()
# errors = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].std()/(len(df.index)**0.5)
# fixtime.plot(kind='bar', yerr=errors, title='Total Fixation Time in AOI by Accuracy')
# plt.ylabel('Fixation Time (ms)')
# plt.show()

# groups = df.groupby(['Session'])
# fixtime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum()
# totaltime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum().sum(axis=1)
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs')
# plt.ylabel('% of Time Fixated in AOIs')
# plt.legend(loc='center right')
# plt.show()
#
# groups = df.groupby(['Session', 'Condition'])
# fixtime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum()
# totaltime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum().sum(axis=1)
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs by Condition')
# plt.ylabel('% of Time Fixated in AOIs')
# plt.legend(loc='center right')
# plt.show()
#
# groups = df.groupby(['Session', 'Accuracy'])
# fixtime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum()
# totaltime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum().sum(axis=1)
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs by Accuracy')
# plt.ylabel('% of Time Fixated in AOIs')
# plt.legend(loc='center right')
# plt.show()
#
######## Fix error bars
# groups = df.groupby('Session')
# trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].mean()
# errors = [[0.112206, 0.079357], [0.108652, 0.073769], [1.433872, 0.859358], [0.257267, 0.210028]]
# #errors = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].std()/(len(df.index)**0.5)
# print errors
# trans.plot(kind='bar', yerr=errors, title='Number of Transitions')
# plt.ylabel('Number of Transitions')
# plt.show()

# groups = df.groupby(['Session', 'Condition'])
# trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].mean()
# errors = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions by Condition')
# plt.ylabel('Number of Transitions')
# plt.legend(loc='upper right')
# plt.show()

# groups = df.groupby(['Session', 'Accuracy'])
# trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].mean()
# errors = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions by Accuracy')
# plt.ylabel('Number of Transitions')
# plt.legend(loc='upper right')
# plt.show()

# groups = df.groupby('Session')
# relation_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum().sum(axis=1)
# relevant_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum()
# prop = relevant_trans.divide(relation_trans, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions')
# plt.ylabel('Percentage of Transitions in AOIs')
# plt.show()

# groups = df.groupby(['Session', 'Accuracy'])
# relation_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum().sum(axis=1)
# relevant_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum()
# prop = relevant_trans.divide(relation_trans, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions by Accuracy')
# plt.ylabel('Percentage of Transitions in AOIs')
# plt.legend(loc='center right')
# plt.show()

# groups = df.groupby(['Session', 'Condition'])
# relation_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum().sum(axis=1)
# relevant_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum()
# prop = relevant_trans.divide(relation_trans, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions by Condition')
# plt.ylabel('Percentage of Transitions in AOIs')
# plt.legend(loc='center right')
# plt.show()

# means = df.groupby(['Training', 'Session']).mean()
# errors = df.groupby(['Training', 'Session'])['Accuracy'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='Accuracy', yerr=errors, title='Accuracy by Training')
# plt.show()
# errors = df.groupby(['Training', 'Session'])['RT_Solving'].std()/(len(df.index)**0.5)
# means.plot(kind='bar', y='RT_Solving', yerr=errors, title='Response Time by Training')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# timeto = groups['TimeToProblem', 'TimeToAnswers'].mean()
# errors = groups['TimeToProblem', 'TimeToAnswers'].std()/(len(df.index)**0.5)
# timeto.plot(kind='bar', yerr=errors, title='Time to First Fixation in AOI by Training')
# plt.ylabel('Time Until First Fixation (ms)')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# timeto = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].mean()
# errors = groups['TotalFixTimeInProblem', 'TotalFixTimeInAnswers'].std()/(len(df.index)**0.5)
# timeto.plot(kind='bar', yerr=errors, title='Total Time Fixated in AOI by Training')
# plt.ylabel('Time Until First Fixation (ms)')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# fixtime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum()
# totaltime = groups[['TotalFixTimeInProblem', 'TotalFixTimeInAnswers']].sum().sum(axis=1)
# prop = fixtime.divide(totaltime, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Proportion of Fixation Time in AOIs by Training')
# plt.ylabel('% of Time Fixated in AOIs')
# plt.legend(loc='center right')
# plt.show()

# groups = df.groupby(['Training', 'Session'])
# trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].mean()
# errors = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].std()/(len(df.index)**0.5)
# trans.plot(yerr=errors, kind='bar', title='Number of Transitions by Training')
# plt.ylabel('Number of Transitions')
# plt.legend(loc='upper right')
# plt.show()
#
# groups = df.groupby(['Training', 'Session'])
# relation_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum().sum(axis=1)
# relevant_trans = groups[['Problem-Answers', 'Answers-Problem', 'Problem-Problem', 'Answers-Answers']].sum()
# prop = relevant_trans.divide(relation_trans, axis='index')
# errors = prop.std()/(len(prop.index)**0.5)
# prop.plot(yerr=errors, kind='bar', title='Percentage of Total Transitions by Training')
# plt.ylabel('Percentage of Transitions in AOIs')
# plt.legend(loc='center right')
# plt.show()
