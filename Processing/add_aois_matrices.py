import pandas as pd
import glob
import os

### Adds AOI and fixation data to the files formatted for Ogama, to be used in defining transitions and making fixation plots

# where to get original files (should be same folder with files that were imported into Ogama)
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Matrices\LSAT_T1\test'
# where to put new files
new_filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Matrices\LSAT_T1\Data_with_AOIs\test'

rules = pd.read_csv('Matrices_Behav_Data/Matrix_Rule_Violation.csv')

for f in glob.glob(filepath + '\*gazedata.csv'):
    filename = os.path.basename(f)
    filename_parts = filename.split('_')
    subject = filename_parts[0]
    block = filename_parts[1]

    print "processing subject:", subject, block

    with open(f, 'r') as csvfile:

        df = pd.read_csv(csvfile, header=None, names=['Index', 'Subject', 'Trial_Num', 'Trial_Index', 'Gaze(x)',
                                                      'Gaze(y)', 'Blink(x)', 'Blink(y)', 'Time', 'Uncertainty', 'Event',
                                                      'Condition', 'Image_File'])
        if block in ['A', 'B']:
            behav = pd.read_csv('Matrices_Behav_Data/LSAT_T1/' + subject + '_Matrices_set' + block + '_behavioralout.txt',
                                delimiter='\t', names=['Trial', 'CorrectAnswer', 'SolutionClicked', 'SubjectResponse',
                                                       'RT_Solving', 'RT_SolvingUnc', 'RT_Response', 'RT_ResponseUnc',
                                                       'OrderSolutions'])
        else:
            behav = pd.read_csv('Matrices_Behav_Data/LSAT_T1/' + subject + '_Matrices_' + block + '_behavioralout.txt',
                                delimiter='\t', names=['Trial', 'CorrectAnswer', 'SolutionClicked', 'SubjectResponse',
                                                       'RT_Solving', 'RT_SolvingUnc', 'RT_Response', 'RT_ResponseUnc',
                                                       'OrderSolutions'])

        image_order = behav['OrderSolutions']

        if len(df) == 0:
            continue

        df = df[1:]     #remove labels from original df
        df = df[df['Event'] == 'gaze'] #ignore blinks

        df.insert(13, 'Fixation', 0)
        df.insert(14, 'AOI_Group', 'nowhere')
        df.insert(15, 'AOI', 'nowhere')
        df.insert(16, 'AOI_Image_Num', None)   #only relevant for points in an Answer AOI
        df.insert(17, 'AOI_Rules_Broken', None)    #only relevant for points in an Answer AOI


        # categorize gaze points into AOIs by coordinates. Record info about the AOI if applicable
        for i in range(len(df.index)):
            if 209 <= float(df['Gaze(x)'].iloc[i]) <= 1064 and 625 <= float(df['Gaze(y)'].iloc[i]) <= 970:
                df['AOI_Group'].iloc[i] = 'Answers'
            elif 306 <= float(df['Gaze(x)'].iloc[i]) <= 970 and 48 <= float(df['Gaze(y)'].iloc[i]) <= 558:
                df['AOI_Group'].iloc[i] = 'Problem'

            if 370 <= float(df['Gaze(x)'].iloc[i]) <= 520 and 54 <= float(df['Gaze(y)'].iloc[i]) <= 204:
                df['AOI'].iloc[i] = 'P1'
            elif 563 <= float(df['Gaze(x)'].iloc[i]) <= 713 and 54 <= float(df['Gaze(y)'].iloc[i]) <= 204:
                df['AOI'].iloc[i] = 'P2'
            elif 756 <= float(df['Gaze(x)'].iloc[i]) <= 906 and 54 <= float(df['Gaze(y)'].iloc[i]) <= 204:
                df['AOI'].iloc[i] = 'P3'
            elif 370 <= float(df['Gaze(x)'].iloc[i]) <= 520 and 209 <= float(df['Gaze(y)'].iloc[i]) <= 359:
                df['AOI'].iloc[i] = 'P4'
            elif 563 <= float(df['Gaze(x)'].iloc[i]) <= 713 and 209 <= float(df['Gaze(y)'].iloc[i]) <= 359:
                df['AOI'].iloc[i] = 'P5'
            elif 756 <= float(df['Gaze(x)'].iloc[i]) <= 906 and 209 <= float(df['Gaze(y)'].iloc[i]) <= 359:
                df['AOI'].iloc[i] = 'P6'
            elif 370 <= float(df['Gaze(x)'].iloc[i]) <= 520 and 364 <= float(df['Gaze(y)'].iloc[i]) <= 514:
                df['AOI'].iloc[i] = 'P7'
            elif 563 <= float(df['Gaze(x)'].iloc[i]) <= 713 and 364 <= float(df['Gaze(y)'].iloc[i]) <= 514:
                df['AOI'].iloc[i] = 'P8'

            elif 247 <= float(df['Gaze(x)'].iloc[i]) <= 397 and 640 <= float(df['Gaze(y)'].iloc[i]) <= 790:
                df['AOI'].iloc[i] = 'A1'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[0]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]
            elif 454 <= float(df['Gaze(x)'].iloc[i]) <= 604 and 640 <= float(df['Gaze(y)'].iloc[i]) <= 790:
                df['AOI'].iloc[i] = 'A2'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[1]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]
            elif 661 <= float(df['Gaze(x)'].iloc[i]) <= 811 and 640 <= float(df['Gaze(y)'].iloc[i]) <= 790:
                df['AOI'].iloc[i] = 'A3'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[2]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]
            elif 868 <= float(df['Gaze(x)'].iloc[i]) <= 1018 and 640 <= float(df['Gaze(y)'].iloc[i]) <= 790:
                df['AOI'].iloc[i] = 'A4'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[3]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]
            elif 247 <= float(df['Gaze(x)'].iloc[i]) <= 397 and 798 <= float(df['Gaze(y)'].iloc[i]) <= 948:
                df['AOI'].iloc[i] = 'A5'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[4]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]
            elif 454 <= float(df['Gaze(x)'].iloc[i]) <= 604 and 798 <= float(df['Gaze(y)'].iloc[i]) <= 948:
                df['AOI'].iloc[i] = 'A6'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[5]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]
            elif 661 <= float(df['Gaze(x)'].iloc[i]) <= 811 and 798 <= float(df['Gaze(y)'].iloc[i]) <= 948:
                df['AOI'].iloc[i] = 'A7'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[6]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]
            elif 306 <= float(df['Gaze(x)'].iloc[i]) <= 970 and 798 <= float(df['Gaze(y)'].iloc[i]) <= 948:
                df['AOI'].iloc[i] = 'A8'
                df['AOI_Image_Num'].iloc[i] = image_order[int(df['Trial_Index'].iloc[i])-1].split(',')[7]
                df['AOI_Rules_Broken'].iloc[i] = rules['Rule_Violation'].iloc[int(df['AOI_Image_Num'].iloc[i])-1]

        # calculate fixations and record them. Fixations are 12 or more points that are not more than 12 pixels apart
        # in the x and y directions
        fixs = []
        counter = 0
        x = list(df['Gaze(x)'])
        y = list(df['Gaze(y)'])
        while len(x) > 1:
            xwindow = x[0:12]
            ywindow = y[0:12]
            if (abs(float(max(xwindow)) - float(min(xwindow))) <= 35) and (abs(float(max(ywindow)) - float(min(ywindow))) <= 35):
                counter += 1
                i = 12
                while (abs(float(max(xwindow)) - float(min(xwindow))) <= 35) and (abs(float(max(ywindow)) - float(min(ywindow))) <= 35) and i < len(x):
                    xwindow.append(x[i])
                    ywindow.append(y[i])
                    i += 1
                fixs += [counter] * (len(xwindow)-1)
                x = x[len(xwindow)-1:]
                y = y[len(ywindow)-1:]
            else:
                x = x[1:]
                y = y[1:]
                fixs += [9999]

        #classify last point
        if len(x) != 0:
            xwindow.append(x[0])
            ywindow.append(y[0])
            if (abs(float(max(xwindow)) - float(min(xwindow))) <= 35) and (abs(float(max(ywindow)) - float(min(ywindow))) <= 35):
                fixs += [counter]
            else:
                fixs += [9999]

        df['Fixation'] = fixs


        df.to_csv(os.path.join(new_filepath, subject + block + '_matrices_gazedata_aois.csv'))
