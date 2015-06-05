import pandas as pd
import glob
import os

filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Matrices\LSAT_T1'
new_filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Matrices\LSAT_T1\Data_with_AOIs'


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

        if len(df) == 0:
            continue

        df = df[1:]     #remove labels from original df
        df = df[df['Event'] == 'gaze']
        df.insert(13, 'AOI', 'nowhere')
        df.insert(14, 'Fixation', 0)


        for i in range(len(df.index)):
            if 209 <= float(df['Gaze(x)'].iloc[i]) <= 1064 and 625 <= float(df['Gaze(y)'].iloc[i]) <= 970:
                df['AOI'].iloc[i] = 'Answers'
            elif 306 <= float(df['Gaze(x)'].iloc[i]) <= 970 and 48 <= float(df['Gaze(y)'].iloc[i]) <= 558:
                df['AOI'].iloc[i] = 'Problem'

            if i < (len(df.index) - 12):
                if (float(max(df['Gaze(x)'].iloc[i:i+12])) - float(min(df['Gaze(x)'].iloc[i:i+12])) <= 35) and (float(max(df['Gaze(y)'].iloc[i:i+12])) - float(min(df['Gaze(y)'].iloc[i:i+12])) <= 35):
                    df['Fixation'].iloc[i:i+12] = 1


        df.to_csv(os.path.join(new_filepath, subject + block + '_matrices_gazedata_aois.csv'))
