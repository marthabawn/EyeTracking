import pandas as pd
import glob
import os

filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Transinf\LSAT_T1'
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
        df = df[df['Event'] == 'gaze']
        df.insert(13, 'AOI', 'nowhere')
        df.insert(14, 'Fixation', 0)


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

            if i < (len(df.index) - 12):
                if (float(max(df['Gaze(x)'].iloc[i:i+12])) - float(min(df['Gaze(x)'].iloc[i:i+12])) <= 35) and (float(max(df['Gaze(y)'].iloc[i:i+12])) - float(min(df['Gaze(y)'].iloc[i:i+12])) <= 35):
                    df['Fixation'].iloc[i:i+12] = 1


        df.to_csv(os.path.join(new_filepath, subject + block + '_transinf_gazedata_aois.csv'))
