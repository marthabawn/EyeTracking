# EyeTracking

- convert_txt_to_xlsx.py creates new xlsx files from all txt files in the given folder. This is slow - use cluster

- create_dataframe.py takes xlsx files and returns a pandas dataframe. It also includes a function to calculate the mean sampling rate
  
- ogama_formatting.py creates dataframe from xlsx files (same code as in create_dataframe.py), puts it in the correct format to be uploaded into Ogama, and writes the dataframe to a csv file. This is slow - use cluster

- ogama_formatting_new.py is the same as above, except it reads data directly from txt files instead of xlsx. Still slow - use cluster

-ogama_formatting_final.py is the final script with all known bugs fixed. The files it produces shouls have no problem being uploaded into Ogama correctly.
