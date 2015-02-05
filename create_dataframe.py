import os
import pandas
import time

#use these functions to create matrix dataframes from the raw files
#the output will be a separate dataframe for each block of trials

#the script runs for one subject at a time
subjid = 118

#specify folder where raw data files are located
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\TrainsInf_data'

def get_files(section):
    #finds all files in specified folder associated with the subject and returns them in a list

    start_time = time.time()
    xlsxfiles = [os.path.join(filepath, f) for f in os.listdir(filepath)
             if os.path.isfile(os.path.join(filepath, f)) and '.xlsx' in f
             and section in f and str(subjid) in f and 'test' in f]

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
    #reads the files and returns a data frame with all data

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

    print ("combine completed in %s seconds" %str(time.time() - start_time))

    return df

def format(df):
    #if necessary, this makes the data frame nicer to work with
    #more intuitive ordering of columns
    #drops duplicate rows (there are usually a lot)
    #fills empty cells with 0

    start_time = time.time()
    cols = df.columns.tolist()
    cols.append(cols[4])    #move 'time' to end
    cols.append(cols[5])    #move 'uncertainty' to end
    cols = cols[:4] + cols[6:]
    df = df[cols]

    df = df.sort('time')
    df = df.drop_duplicates(cols)
    df = df.reset_index()
    df = df.drop('index', axis=1)
    df = df.fillna(value=0)

    print ("format completed in %s seconds" %str(time.time() - start_time))

    return df

def get_sampling_rate(df):
    #finds mean sampling rate for the block of data

    n = len(df.index)   #number of rows
    total_time = df['time'].iloc[n-1] - df['time'].iloc[0]
    sampling_rate = total_time / n

    return sampling_rate


if __name__ == '__main__':
    #add another for loop here to do multiple subjects
    for section in ['practice']:    #if running all files for one subject, the list should be ['practice', 'setA', 'setB']
        files = get_files(section)

        gazefiles = files[0]
        pupilfiles = files[1]
        blinkfiles = files[2]

        df = combine(gazefiles, pupilfiles, blinkfiles)
        df = format(df)

        sampling_rate = get_sampling_rate(df)
        print "the mean sampling rate for subject " + str(subjid) + ' in ' + section + ' block is ' + str(sampling_rate) + ' milliseconds'

        #save, catalog or further process each dataframe here
