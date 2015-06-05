import os
import pandas
import time
 
#subjid = 111
#section = 'B'
 
filepath =  '/home/bunge/bguerra/EyeTracking/Raw_Data/Transinf_data/LSAT_T2'
 
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
 
 
def combine(gazefile, pupilfile, blinkfile):
    start_time = time.time()
    gazefile = pandas.read_csv(gazefile, delim_whitespace=True, header=None)
    #pupilfile = pandas.read_csv(pupilfile, delim_whitespace=True, header=None)
    blinkfile = pandas.read_csv(blinkfile, delim_whitespace=True, header=None)
 
 
    df1 = gazefile
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
 
def add_descriptive_cols(df):
    start_time = time.time()
    #add column for subject id
    subjid_col = ['tp' + str(subjid) + section] * len(df.index)
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

	#use this for subjects where the numbering is off (trial numbers start at 2)
    	#df['trial_number'].iloc[i] -= 1
 
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
        if section == 'A':
            if df['trial_number'].iloc[i] in [1, 4, 17, 24, 25]:
                df['condition'].iloc[i] = '1'   #Inequality/Equality, 0 apart
                df['image_file'].iloc[i] = 'Slide1.bmp'
            elif df['trial_number'].iloc[i] in [7, 13, 16, 26, 29]:
                df['condition'].iloc[i] = '2'   #Inequality/Equality, 1 apart
                df['image_file'].iloc[i] = 'Slide2.bmp'
            elif df['trial_number'].iloc[i] in [5, 6, 11, 14, 19]:
                df['condition'].iloc[i] = '3'   #Inequality/Equality, 2 apart
                df['image_file'].iloc[i] = 'Slide3.bmp'
            elif df['trial_number'].iloc[i] in [2, 15, 21, 22, 27]:
                df['condition'].iloc[i] = '4'   #Inequality/Inequality, 0 apart
                df['image_file'].iloc[i] = 'Slide4.bmp'
            elif df['trial_number'].iloc[i] in [8, 12, 18, 28, 30]:
                df['condition'].iloc[i] = '5'   #Inequality/Inequality, 1 apart
                df['image_file'].iloc[i] = 'Slide5.bmp'
            elif df['trial_number'].iloc[i] in [3, 9, 10, 20, 23]:
                df['condition'].iloc[i] = '6'   #Inequality/Inequality, 2 apart
                df['image_file'].iloc[i] = 'Slide6.bmp'
        elif section == 'B':
            if df['trial_number'].iloc[i] in [8, 22, 23, 24, 30]:
                df['condition'].iloc[i] = '1'   #Inequality/Equality, 0 apart
                df['image_file'].iloc[i] = 'Slide1.bmp'
            elif df['trial_number'].iloc[i] in [1, 7, 13, 15, 19]:
                df['condition'].iloc[i] = '2'   #Inequality/Equality, 1 apart
                df['image_file'].iloc[i] = 'Slide2.bmp'
            elif df['trial_number'].iloc[i] in [3, 21, 26, 28, 29]:
                df['condition'].iloc[i] = '3'   #Inequality/Equality, 2 apart
                df['image_file'].iloc[i] = 'Slide3.bmp'
            elif df['trial_number'].iloc[i] in [2, 4, 10, 11, 12]:
                df['condition'].iloc[i] = '4'   #Inequality/Inequality, 0 apart
                df['image_file'].iloc[i] = 'Slide4.bmp'
            elif df['trial_number'].iloc[i] in [6, 9, 14, 18, 20]:
                df['condition'].iloc[i] = '5'   #Inequality/Inequality, 1 apart
                df['image_file'].iloc[i] = 'Slide5.bmp'
            elif df['trial_number'].iloc[i] in [5, 16, 17, 25, 27]:
                df['condition'].iloc[i] = '6'   #Inequality/Inequality, 2 apart
                df['image_file'].iloc[i] = 'Slide6.bmp'
        elif section == 'practice':
            df['condition'].iloc[i] = '1'   #Inequality/Equality, 0 apart
            df['image_file'].iloc[i] = 'Slide1.bmp'
 
    print ("add_descriptive_cols completed in %s seconds" %str(time.time() - start_time))
 
    return df
 
 
if __name__ == '__main__':
    new_filepath = '/home/bunge/bguerra/EyeTracking/Raw_Data/OgamaProcessing/LSAT_T2/transinf'
    for subjid in [202, 203]:
        for section in ['practice', 'A', 'B']:
	    try:
		files = get_files(subjid, section)

		gazefile = files[0]
		pupilfile = files[1]
		blinkfile = files[2]

		df = combine(gazefile, pupilfile, blinkfile)
		df = format(df)
		df = add_descriptive_cols(df)

		df.to_csv(os.path.join(new_filepath, 'tp' + str(subjid) + section + '_transinf_gazedata.csv'))
		print str(subjid) + section + ' file created'
	    except:
		print 'Failed for subject ' + str(subjid)
