import os
import pandas
import time

### Takes raw data files from Presentation and formats them for importing to Ogama

# Where to get raw files
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Matrices_data\LSAT_T2'

# get all files in the filepath folder
def get_files(subjid, section):
    start_time = time.time()
    txtfiles = [os.path.join(filepath, f) for f in os.listdir(filepath)
             if os.path.isfile(os.path.join(filepath, f)) and '.txt' in f
             and section in f and str(subjid) in f]

    gazefile = ''
    pupilfile = ''
    blinkfile = ''

    for txtfile in txtfiles:
        if 'gaze' in txtfile:
            gazefile = txtfile
        if 'pupil' in txtfile:
            pupilfile = txtfile
        if 'blink' in txtfile:
            blinkfile = txtfile

    print gazefile
    print pupilfile
    print blinkfile

    print ("get_files completed in %s seconds" %str(time.time() - start_time))

    return [gazefile, pupilfile, blinkfile]

# combine all three trials into one dataframe, no longer using the pupil file
def combine(gazefile, pupilfile, blinkfile):
    start_time = time.time()
    gazefile = pandas.read_csv(gazefile, delim_whitespace=True, header=None)
    #pupilfile = pandas.read_csv(pupilfile, delim_whitespace=True, header=None)
    blinkfile = pandas.read_csv(blinkfile, delim_whitespace=True, header=None)


    df1 = gazefile.iloc[:, 0:6]
    df1.columns = ['trial_number', 'trial_index', 'gaze(x)', 'gaze(y)', 'time', 'uncertainty']

    #df2 = pupilfile
    #df2.columns = ['trial_number', 'trial_index', 'pupil(x)', 'pupil(y)', 'time', 'uncertainty']

    df3 = blinkfile
    df3.columns = ['trial_number', 'trial_index', 'blink(x)', 'blink(y)', 'time', 'uncertainty']

    #df4 = pandas.merge(df1, df2, how='outer', sort=True)
    #df = pandas.merge(df4, df3, how='outer', sort=True)

    df = pandas.merge(df1, df3, how='outer', sort=True)
    df[['trial_number', 'trial_index']] = df[['trial_number', 'trial_index']].astype(int)

    print ("combine completed in %s seconds" %str(time.time() - start_time))

    return df

# rearrange columns, sort by Time, drop duplicate rows
def format(df):
    start_time = time.time()
    cols = df.columns.tolist()
    cols.append(cols[4])    #move 'time' to end
    cols.append(cols[5])    #move 'uncertainty' to end
    cols = cols[:4] + cols[6:]
    df = df[cols]

    df = df.sort('time')
    df = df.drop_duplicates(cols)
    #if getting MemoryError, use this - since it's sorted it does the same thing
    #for i in range(len(df.index)-1):
        #if df.iloc[i,:].all() == df.iloc[i+1,:].all():
		    #df = df.drop([i])
    df = df.reset_index()
    df.index += 1
    df = df.drop('index', axis=1)
    df = df.fillna(value=0)

    print ("format completed in %s seconds" %str(time.time() - start_time))

    return df

# add columns for condition, event, and image_file, change coordinates to Ogama's system
def add_descriptive_cols(df):
    start_time = time.time()
    #add column for subject id
    subjid_col = ['tp' + str(subjid) + section] * len(df.index)
    df.insert(0, 'subject', subjid_col)

    df['event'] = 0
    df['condition'] = 1
    df['image_file'] = 'matrix_slide.bmp'


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

        #trial index should start at 1, not 0
        df['trial_index'].iloc[i] = df['trial_index'].iloc[i] + 1

    print ("add_descriptive_cols completed in %s seconds" %str(time.time() - start_time))

    return df

# run everything
if __name__ == '__main__':
    # where to save the new files
    new_filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\Ogama_Processed_Data\Matrices\LSAT_T2'
    # change list to reflect which subjects to process
    for subjid in [202, 203, 206, 207, 209, 210, 213, 215]:
        try:
            for section in ['A', 'B', 'practice']:
                files = get_files(subjid, section)
                gazefile = files[0]
                pupilfile = files[1]
                blinkfile = files[2]

                df = combine(gazefile, pupilfile, blinkfile)
                df = format(df)
                df = add_descriptive_cols(df)

                df.to_csv(os.path.join(new_filepath, 'tp' + str(subjid) + '_' + section + '_matrices_gazedata.csv'))
                print str(subjid) + section + ' file created'
        except:
            print 'Failed for subject ' + str(subjid) + '_' + section
