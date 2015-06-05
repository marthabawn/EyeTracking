import numpy as np
import pandas as pd
import glob
import os

dict_practice = {1: '1', 2: '1'}

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

df = pd.DataFrame()

#Reads all the _behavioral files in the folder specified
for f in glob.glob("TransInf/*behavioralout.txt"):
	filename = os.path.basename(f)
	filename_parts = filename.split('_')
	subject = filename_parts[0][:5]
	block = filename_parts[2]
	group = filename_parts[0][:2]

	print "processing subject:", subject, block

	with open(f, 'r') as csvfile:
		
		dfTemp = pd.read_csv(csvfile, delimiter='\t', header=None, names=['Trial', 'Infer', 'CorrectAnswer', 'SubjectResponse', 'ProbRel', 'RT', 'RT_Unc'] )
		
		if len(dfTemp) == 0:
			continue

		dfTemp.insert(0, 'PID', subject)
		dfTemp.insert(1, 'Group', group)
		dfTemp.insert(2, 'Block', block)
		dfTemp['Accuracy'] = np.where(dfTemp['CorrectAnswer'] == dfTemp['SubjectResponse'], 1, 0)

		dfNewCol = dfTemp.apply(map_trial_to_condition, axis=1)
		dfTemp.insert(3, 'Condition', dfNewCol)

		df = df.append(dfTemp, ignore_index=True)
