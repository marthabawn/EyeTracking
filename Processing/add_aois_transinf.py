import pandas as pd
import glob
import os

### Adds AOI and fixation data to the files formatted for Ogama, to be used in defining transitions and making fixation plots

# where to get original files (should be same folder with files that were imported into Ogama)
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Transinf\LSAT_T1'
# where to put new files
new_filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Transinf\LSAT_T1\Data_with_AOIs'


for f in glob.glob(filepath + '\*gazedata.csv'):
    filename = os.path.basename(f)
    filename_parts = filename.split('_')
    subject = filename_parts[0][:5]
    block = filename_parts[0][5:]

    print "processing subject:", subject, block

    with open(f, 'r') as csvfile:

        df = pd.read_csv(csvfile, header=None, names=['Index', 'Subject', 'Trial_Num', 'Trial_Index', 'Gaze(x)',
                                                      'Gaze(y)', 'Blink(x)', 'Blink(y)', 'Time', 'Uncertainty', 'Event',
                                                      'Condition', 'Image_File'])

        if len(df) == 0:
            continue

        df = df[1:]     #remove labels from original df
        df = df[df['Event'] == 'gaze']  # ignore blinks
        df.insert(13, 'AOI', 'nowhere')
        df.insert(14, 'Fixation', 0)

        # categorize gaze points into AOIs by coordinates
        for i in range(len(df.index)):
            if 400 <= float(df['Gaze(x)'].iloc[i]) <= 792 and 625 <= float(df['Gaze(y)'].iloc[i]) <= 875:
                df['AOI'].iloc[i] = 'Q'
            elif 65 <= float(df['Gaze(x)'].iloc[i]) <= 318 and 178 <= float(df['Gaze(y)'].iloc[i]) <= 472:
                if df['Condition'].iloc[i] in ['2', '3', '6']:
                    df['AOI'].iloc[i] = 'Rel1'
                else:
                    df['AOI'].iloc[i] = 'Irrel1'
            elif 348 <= float(df['Gaze(x)'].iloc[i]) <= 601 and 178 <= float(df['Gaze(y)'].iloc[i]) <= 472:
                if df['Condition'].iloc[i] in ['1', '5']:
                    df['AOI'].iloc[i] = 'Rel1'
                elif df['Condition'].iloc[i] == '4':
                    df['AOI'].iloc[i] = 'Irrel2'
                else:
                    df['AOI'].iloc[i] = 'Irrel1'
            elif 631 <= float(df['Gaze(x)'].iloc[i]) <= 884 and 178 <= float(df['Gaze(y)'].iloc[i]) <= 472:
                if df['Condition'].iloc[i] in ['1', '2']:
                    df['AOI'].iloc[i] = 'Rel2'
                elif df['Condition'].iloc[i] == '4':
                    df['AOI'].iloc[i] = 'Rel1'
                else:
                    df['AOI'].iloc[i] = 'Irrel2'
            elif 914 <= float(df['Gaze(x)'].iloc[i]) <= 1167 and 178 <= float(df['Gaze(y)'].iloc[i]) <= 472:
                if df['Condition'].iloc[i] in ['3', '4', '5', '6']:
                    df['AOI'].iloc[i] = 'Rel2'
                else:
                    df['AOI'].iloc[i] = 'Irrel2'

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
                i = 12
                while (abs(float(max(xwindow)) - float(min(xwindow))) <= 35) and (abs(float(max(ywindow)) - float(min(ywindow)))) <= 35 and i < len(x):
                    xwindow.append(x[i])
                    ywindow.append(y[i])
                    i += 1
                counter += 1
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


        df.to_csv(os.path.join(new_filepath, subject + block + '_transinf_gazedata_aois.csv'))
