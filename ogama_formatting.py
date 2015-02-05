import os
import pandas
import time

subjid = 118

filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\TrainsInf_data'

def get_files(section):
    start_time = time.time()
    xlsxfiles = [os.path.join(filepath, f) for f in os.listdir(filepath)
             if os.path.isfile(os.path.join(filepath, f)) and '.xlsx' in f
             and section in f and str(subjid) in f and 'test' not ain f]

    gazefiles = []
    pupilfiles = []
    blinkfiles = []

    for xlsxfile in xlsxfiles:
        if 'gaze' in xlsxfile:
            gazefiles.append(xlsxfile)
        if 'pupil' in xlsxfile:
            pupilfiles.append(xlsxfile)
        if 'blink' in xlsxfile:
            blinkfiles.append(xlsxfile)

    print gazefiles
    print pupilfiles
    print blinkfiles

    print ("get_files completed in %s seconds" %str(time.time() - start_time))

    return [gazefiles, pupilfiles, blinkfiles]


def combine(gazefiles, pupilfiles, blinkfiles):
    start_time = time.time()
    for i in range(len(gazefiles)):
        gazefiles[i] = pandas.read_excel(gazefiles[i], 'Sheet1', header=None)
    for i in range(len(pupilfiles)):
        pupilfiles[i] = pandas.read_excel(pupilfiles[i], 'Sheet1', header=None)
    for i in range(len(blinkfiles)):
        blinkfiles[i] = pandas.read_excel(blinkfiles[i], 'Sheet1', header=None)


    if len(gazefiles) > 1:
        df1 = pandas.concat(gazefiles)
    else:
        df1 = gazefiles[0]
    df1.columns = ['trial number', 'trial index', 'gaze(x)', 'gaze(y)', 'time', 'uncertainty']

    if len(pupilfiles) > 1:
        df2 = pandas.concat(pupilfiles)
    else:
        df2 = pupilfiles[0]
    df2.columns = ['trial number', 'trial index', 'pupil(x)', 'pupil(y)', 'time', 'uncertainty']

    if len(blinkfiles) > 1:
        df3 = pandas.concat(blinkfiles)
    else:
        df3 = blinkfiles[0]
    df3.columns = ['trial number', 'trial index', 'blink(x)', 'blink(y)', 'time', 'uncertainty']

    df4 = pandas.merge(df1, df2, how='outer', sort=True)
    df = pandas.merge(df4, df3, how='outer', sort=True)
    df[['trial number', 'trial index']] = df[['trial number', 'trial index']].astype(int)

    print ("combine completed in %s seconds" %str(time.time() - start_time))

    return df

def format(df):
    start_time = time.time()
    cols = df.columns.tolist()
    cols.append(cols[4])    #move 'time' to end
    cols.append(cols[5])    #move 'uncertainty' to end
    cols = cols[:4] + cols[6:]
    df = df[cols]

    df = df.sort('time')
    df = df.drop_duplicates(cols)
    df = df.reset_index()
    df.index += 1
    df = df.drop('index', axis=1)
    df = df.fillna(value=0)

    print ("format completed in %s seconds" %str(time.time() - start_time))

    return df

def add_descriptive_cols(df):
    start_time = time.time()
    #add column for subject id
    subjid_col = ['rt' + str(subjid)] * len(df.index)
    df.insert(0, 'subject', subjid_col)

    df['event'] = 0
    df['condition'] = 0
    df['image_file'] = 0


    for i in range(len(df.index)):
        #add column for event at each time
        if df['blink(x)'].iloc[i] != 0 and df['gaze(x)'].iloc[i] == 0:
            df['event'].iloc[i] = 'blink'
        elif df['blink(x)'].iloc[i] != 0 and df['gaze(x)'].iloc[i] != 0:
            df['event'].iloc[i] = 'gaze/blink'
        else:
            df['event'].iloc[i] = 'gaze'

        #change coordinates from origin in center to origin in top left with inverted y axis
        if df['event'].iloc[i] != 'blink':
            df['gaze(x)'].iloc[i] += 640
            df['gaze(y)'].iloc[i] *= -1
            df['gaze(y)'].iloc[i] += 512
        elif df['event'].iloc[i] != 'gaze':
            df['blink(x)'].iloc[i] += 640
            df['blink(y)'].iloc[i] *= -1
            df['blink(y)'].iloc[i] += 512


        #add columns for condition number and image file name
        if section == 'setA':
            if df['trial number'].iloc[i] in [1, 4, 17, 24, 25]:
                df['condition'].iloc[i] = 'IE0'   #Inequality/Equality, 0 apart
                df['image_file'].iloc[i] = 'Slide1.bmp'
            elif df['trial number'].iloc[i] in [7, 13, 16, 26, 29]:
                df['condition'].iloc[i] = 'IE1'   #Inequality/Equality, 1 apart
                df['image_file'].iloc[i] = 'Slide2.bmp'
            elif df['trial number'].iloc[i] in [5, 6, 11, 14, 19]:
                df['condition'].iloc[i] = 'IE2'   #Inequality/Equality, 2 apart
                df['image_file'].iloc[i] = 'Slide3.bmp'
            elif df['trial number'].iloc[i] in [2, 15, 21, 22, 27]:
                df['condition'].iloc[i] = 'II0'   #Inequality/Inequality, 0 apart
                df['image_file'].iloc[i] = 'Slide4.bmp'
            elif df['trial number'].iloc[i] in [8, 12, 18, 28, 30]:
                df['condition'].iloc[i] = 'II1'   #Inequality/Inequality, 1 apart
                df['image_file'].iloc[i] = 'Slide5.bmp'
            elif df['trial number'].iloc[i] in [3, 9, 10, 20, 23]:
                df['condition'].iloc[i] = 'II2'   #Inequality/Inequality, 2 apart
                df['image_file'].iloc[i] = 'Slide6.bmp'
        elif section == 'setB':
            if df['trial number'].iloc[i] in [8, 22, 23, 24, 30]:
                df['condition'].iloc[i] = 'IE0'   #Inequality/Equality, 0 apart
                df['image_file'].iloc[i] = 'Slide1.bmp'
            elif df['trial number'].iloc[i] in [1, 7, 13, 15, 19]:
                df['condition'].iloc[i] = 'IE1'   #Inequality/Equality, 1 apart
                df['image_file'].iloc[i] = 'Slide2.bmp'
            elif df['trial number'].iloc[i] in [3, 21, 26, 28, 29]:
                df['condition'].iloc[i] = 'IE2'   #Inequality/Equality, 2 apart
                df['image_file'].iloc[i] = 'Slide3.bmp'
            elif df['trial number'].iloc[i] in [2, 4, 10, 11, 12]:
                df['condition'].iloc[i] = 'II0'   #Inequality/Inequality, 0 apart
                df['image_file'].iloc[i] = 'Slide4.bmp'
            elif df['trial number'].iloc[i] in [6, 9, 14, 18, 20]:
                df['condition'].iloc[i] = 'II1'   #Inequality/Inequality, 1 apart
                df['image_file'].iloc[i] = 'Slide5.bmp'
            elif df['trial number'].iloc[i] in [5, 16, 17, 25, 27]:
                df['condition'].iloc[i] = 'II2'   #Inequality/Inequality, 2 apart
                df['image_file'].iloc[i] = 'Slide6.bmp'
        elif section == 'practice':
            df['condition'].iloc[i] = 'IE0'   #Inequality/Equality, 0 apart
            df['image_file'].iloc[i] = 'Slide1.bmp'

    print ("add_descriptive_cols completed in %s seconds" %str(time.time() - start_time))

    return df


if __name__ == '__main__':
    for section in ['practice']:
        files = get_files(section)

        gazefiles = files[0]
        pupilfiles = files[1]
        blinkfiles = files[2]

        df = combine(gazefiles, pupilfiles, blinkfiles)
        df = format(df)
        df = add_descriptive_cols(df)

        df.to_csv(os.path.join(filepath, 'rt' + str(subjid) + '_' + section + '_transinf_gazedata_test.csv'))
        print 'file created'
