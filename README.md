# EyeTracking

NOTE: Most up-to-date versions are in Ogama_formatting, Processing, Looking_at_data

- convert_txt_to_xlsx.py creates new xlsx files from all txt files in the given folder. This is slow - use cluster

- create_dataframe.py takes xlsx files and returns a pandas dataframe. It also includes a function to calculate the mean sampling rate

- ogama_formatting.py creates dataframe from xlsx files (same code as in create_dataframe.py), puts it in the correct format to be uploaded into Ogama, and writes the dataframe to a csv file. This is slow - use cluster

- ogama_formatting_new.py is the same as above, except it reads data directly from txt files instead of xlsx. Still slow - use cluster

- transinf_ogama.py is the final script with all known bugs fixed. The files it produces should have no problem being uploaded into Ogama correctly.

- matrices_ogama.py creates pandas dataframe from txt files, formats it for Ogama, and saves it to a csv file.

- behav_gaze_df_transinf.py creates a dataframe with the transinf behavioral data and the gaze statistics exported from Ogama

- behav_gaze_df_matrices.py creates a dataframe with the matrices behavioral data and the gaze statistics exported from Ogama

- matrices_behav_gaze_combine1-9.py does the same as above, but allows for the missing columns in the first rpp participants

- add_aois_matrices.py and add_aois_transinf.py add fixation information to the Ogama formatted files

- define_transitions_matrices.py and define_transitions_transinf.py calculate fixations and transitions from the files with AOI information

- graph_data.py creates graphs for both tasks

- stat_analysis.py runs t-test for both tasks

- fixation_plot files create fixation plots, modified from Mike's script

The folders and files required to run these last 3 are in the Dropbox scripts folder
