# EyeTracking

convert_txt_to_xlsx.py creates new xlsx files from all txt files in the given folder. This is slow - use cluster

create_dataframe.py takes xlsx files and returns a pandas dataframe. It also includes a function to calculate the mean sampling rate
  
ogama_formatting.py creates dataframe from xlsx files (same code as in create_dataframe.py), puts it in the correct format to be uploaded into Ogama, and writes the dataframe to a csv file. This is slow - use cluster
