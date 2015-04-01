import os
import pandas as pd

#change here to access different sections of transition data
filepath = r'C:\Users\bungelab\Documents\OgamaExperiments\Martha\Statistics_exports\matrices_stats\RPP\GroupTransitions'
group = 'RPP'
task = 'matrices'   #'transinf' or 'matrices'
data = 'group'    #'AOI' or 'group'
size = 12   #42 for transinf/AOI, 42 for transinf/group, 306 for matrices/AOI, 12 for matrices/group

txtfiles = [os.path.join(filepath, f) for f in os.listdir(filepath)
            if os.path.isfile(os.path.join(filepath, f)) and '.txt' in f]

filenames = [os.path.basename(txtfile) for txtfile in txtfiles]
trans_matrices = [pd.read_csv(txtfile, delimiter='\t') for txtfile in txtfiles]

# Ogama adds an empty column and row to the end
trans_matrices = [matrix.dropna(axis=1, how='all') for matrix in trans_matrices]
trans_matrices = [matrix.dropna(how='all') for matrix in trans_matrices]

trans_matrices = [matrix.as_matrix().transpose() for matrix in trans_matrices]

trans_vectors = [pd.Series(matrix.reshape(size)) for matrix in trans_matrices]

dict = {}
if task == 'transinf' and data == 'AOI':
    for i in range(len(filenames)):
        subj = filenames[i].split('_')[0]
        cond = filenames[i].split('_')[-1][0:5]
        dict[(subj, cond)] = trans_vectors[i][6:]

    df = pd.DataFrame(dict).transpose()
    df.columns = ['Nowhere-Nowhere', 'Nowhere-Q', 'Nowhere-R1', 'Nowhere-R2', 'Nowhere-R3', 'Nowhere-R4', 'Q-Nowhere',
                  'Q-Q', 'Q-R1', 'Q-R2', 'Q-R3', 'Q-R4', 'R1-Nowhere', 'R1-Q', 'R1-R1', 'R1-R2', 'R1-R3', 'R1-R4',
                  'R2-Nowhere', 'R2-Q', 'R2-R1', 'R2-R2', 'R2-R3', 'R2-R4', 'R3-Nowhere', 'R3-Q', 'R3-R1', 'R3-R2',
                  'R3-R3', 'R3-R4', 'R4-Nowhere', 'R4-Q', 'R4-R1', 'R4-R2', 'R4-R3', 'R4-R4']
    df.to_csv(os.path.join(filepath, group + '_' + task + '_transitions_' + data + '_all_transitions.csv'))

if task == 'transinf' and data == 'group':
    for i in range(len(filenames)):
        subj = filenames[i].split('_')[0]
        dict[subj] = pd.Series(trans_vectors[i][j] for j in [6, 7, 10, 11, 12, 13, 16, 17, 30, 31, 34, 35, 36, 37, 40, 41])

    df = pd.DataFrame(dict).transpose()
    df.columns = ['Nowhere-Nowhere', 'Nowhere-Target', 'Nowhere-Question', 'Nowhere-NonTarget', 'Target-Nowhere',
                  'Target-Target', 'Target-Question', 'Target-NonTarget', 'Question-Nowhere', 'Question-Target',
                  'Question-Question', 'Question-NonTarget', 'NonTarget-Nowhere', 'NonTarget-Target',
                  'NonTarget-Question', 'NonTarget-NonTarget']
    df.to_csv(os.path.join(filepath, group + '_' + task + '_transitions_' + data + '_all_transitions.csv'))

if task == 'matrices' and data == 'AOI':
    for i in range(len(filenames)):
        subj = filenames[i].split('_')[0]
        dict[subj] = trans_vectors[i][17:]

    df = pd.DataFrame(dict).transpose()
    df.columns = ['Nowhere-A1', 'Nowhere-A2', 'Nowhere-A3', 'Nowhere-A4', 'Nowhere-A5', 'Nowhere-A6', 'Nowhere-A7',
                  'Nowhere-A8','Nowhere-Nowhere', 'Nowhere-P1', 'Nowhere-P2', 'Nowhere-P3', 'Nowhere-P4', 'Nowhere-P5',
                  'Nowhere-P6', 'Nowhere-P7', 'Nowhere-P8', 'P1-A1', 'P1-A2', 'P1-A3', 'P1-A4', 'P1-A5', 'P1-A6',
                  'P1-A7', 'P1-A8', 'P1-Nowhere', 'P1-P1', 'P1-P2', 'P1-P3', 'P1-P4', 'P1-P5', 'P1-P6', 'P1-P7',
                  'P1-P8', 'P2-A1', 'P2-A2', 'P2-A3', 'P2-A4', 'P2-A5', 'P2-A6', 'P2-A7', 'P2-A8', 'P2-Nowhere',
                  'P2-P1', 'P2-P2', 'P2-P3', 'P2-P4', 'P2-P5', 'P2-P6', 'P2-P7', 'P2-P8', 'P3-A1', 'P3-A2', 'P3-A3',
                  'P3-A4', 'P3-A5', 'P3-A6', 'P3-A7', 'P3-A8', 'P3-Nowhere', 'P3-P1', 'P3-P2', 'P3-P3', 'P3-P4',
                  'P3-P5', 'P3-P6', 'P3-P7', 'P3-P8', 'P4-A1', 'P4-A2', 'P4-A3', 'P4-A4', 'P4-A5', 'P4-A6', 'P4-A7',
                  'P4-A8', 'P4-Nowhere', 'P4-P1', 'P4-P2', 'P4-P3', 'P4-P4', 'P4-P5', 'P4-P6', 'P4-P7', 'P4-P8',
                  'P5-A1', 'P5-A2', 'P5-A3', 'P5-A4', 'P5-A5', 'P5-A6', 'P5-A7', 'P5-A8', 'P5-Nowhere', 'P5-P1',
                  'P5-P2', 'P5-P3', 'P5-P4', 'P5-P5', 'P5-P6', 'P5-P7', 'P5-P8', 'P6-A1', 'P6-A2', 'P6-A3', 'P6-A4',
                  'P6-A5', 'P6-A6', 'P6-A7', 'P6-A8', 'P6-Nowhere', 'P6-P1', 'P6-P2', 'P6-P3', 'P6-P4', 'P6-P5',
                  'P6-P6', 'P6-P7', 'P6-P8', 'P7-A1', 'P7-A2', 'P7-A3', 'P7-A4', 'P7-A5', 'P7-A6', 'P7-A7', 'P7-A8',
                  'P7-Nowhere', 'P7-P1', 'P7-P2', 'P7-P3', 'P7-P4', 'P7-P5', 'P7-P6', 'P7-P7', 'P7-P8', 'P8-A1',
                  'P8-A2', 'P8-A3', 'P8-A4', 'P8-A5', 'P8-A6', 'P8-A7', 'P8-A8', 'P8-Nowhere', 'P8-P1', 'P8-P2',
                  'P8-P3', 'P8-P4', 'P8-P5', 'P8-P6', 'P8-P7', 'P8-P8',  'A1-A1', 'A1-A2', 'A1-A3', 'A1-A4', 'A1-A5',
                  'A1-A6', 'A1-A7', 'A1-A8', 'A1-Nowhere', 'A1-P1', 'A1-P2', 'A1-P3', 'A1-P4', 'A1-P5', 'A1-P6',
                  'A1-P7', 'A1-P8', 'A2-A1', 'A2-A2', 'A2-A3', 'A2-A4', 'A2-A5', 'A2-A6', 'A2-A7', 'A2-A8',
                  'A2-Nowhere', 'A2-P1', 'A2-P2', 'A2-P3', 'A2-P4', 'A2-P5', 'A2-P6', 'A2-P7', 'A2-P8', 'A3-A1',
                  'A3-A2', 'A3-A3', 'A3-A4', 'A3-A5', 'A3-A6', 'A3-A7', 'A3-A8', 'A3-Nowhere', 'A3-P1', 'A3-P2',
                  'A3-P3', 'A3-P4', 'A3-P5', 'A3-P6', 'A3-P7', 'A3-P8', 'A4-A1', 'A4-A2', 'A4-A3', 'A4-A4', 'A4-A5',
                  'A4-A6', 'A4-A7', 'A4-A8', 'A4-Nowhere', 'A4-P1', 'A4-P2', 'A4-P3', 'A4-P4', 'A4-P5', 'A4-P6',
                  'A4-P7', 'A4-P8', 'A5-A1', 'A5-A2', 'A5-A3', 'A5-A4', 'A5-A5', 'A5-A6', 'A5-A7', 'A5-A8',
                  'A5-Nowhere', 'A5-P1', 'A5-P2', 'A5-P3', 'A5-P4', 'A5-P5', 'A5-P6', 'A5-P7', 'A5-P8', 'A6-A1',
                  'A6-A2', 'A6-A3', 'A6-A4', 'A6-A5', 'A6-A6', 'A6-A7', 'A6-A8', 'A6-Nowhere', 'A6-P1', 'A6-P2',
                  'A6-P3', 'A6-P4', 'A6-P5', 'A6-P6', 'A6-P7', 'A6-P8', 'A7-A1', 'A7-A2', 'A7-A3', 'A7-A4', 'A7-A5',
                  'A7-A6', 'A7-A7', 'A7-A8', 'A7-Nowhere', 'A7-P1', 'A7-P2', 'A7-P3', 'A7-P4', 'A7-P5', 'A7-P6',
                  'A7-P7', 'A7-P8', 'A8-A1', 'A8-A2', 'A8-A3', 'A8-A4', 'A8-A5', 'A8-A6', 'A8-A7', 'A8-A8',
                  'A8-Nowhere', 'A8-P1', 'A8-P2', 'A8-P3', 'A8-P4', 'A8-P5', 'A8-P6', 'A8-P7', 'A8-P8']
    df.to_csv(os.path.join(filepath, group + '_' + task + '_transitions_' + data + '_all_transitions.csv'))

if task == 'matrices' and data == 'group':
    for i in range(len(filenames)):
        subj = filenames[i].split('_')[0]
        dict[subj] = trans_vectors[i][3:]

    df = pd.DataFrame(dict).transpose()
    df.columns = ['Nowhere-Nowhere', 'Nowhere-Problem', 'Nowhere-Answers', 'Problem-Nowhere', 'Problem-Problem',
                  'Problem-Answers', 'Answers-Nowhere', 'Answers-Problem', 'Answers_Answers']
    df.to_csv(os.path.join(filepath, group + '_' + task + '_transitions_' + data + '_all_transitions.csv'))

