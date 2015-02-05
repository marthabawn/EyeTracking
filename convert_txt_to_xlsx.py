import os
import xlsxwriter

#put files to be converted into temp folder
filepath = r'C:\Users\bungelab\Desktop\ReasoningTraining-EyeTracking\DataBackup\temp'
textfiles = [os.path.join(filepath, f) for f in os.listdir(filepath)
             if os.path.isfile(os.path.join(filepath, f)) and '.txt' in f]


def split_file(infilepath, lines_per_file=1048575):
    #check for files longer than Excel's limit and split them into smaller files
    #limit for .xlsx is 1048575
    #limit for .xls is 65535

    path, filename = os.path.split(infilepath)
    basename, ext = os.path.splitext(filename)

    lines = open(infilepath, 'rb').readlines()

    #check if file needs to be split
    if len(lines) > lines_per_file:
        outputname = os.path.join(path, '{}_{}{}'.format(basename, 1, ext))
        outfile = open(outputname, 'w')
        filecount = 1

        for i, line in enumerate(lines):
            #when current line can be divided by the line count, close the output file and open the next one
            if i % lines_per_file == 0:
                outfile.close()
                outputname = os.path.join(path, '{}_{}{}'.format(basename, filecount, ext))
                outfile = open(outputname, 'w')
                filecount += 1
            outfile.write(line)

        os.remove(infilepath)
        outfile.close()


def convert_all_files(textfiles):
    #make a copy of all .txt files in .xlsx format

    for textfile in textfiles:
        f = open(textfile, 'r+')
        row_list = []

        for row in f:
            row_list.append(row.split('\t'))
        column_list = zip(*row_list)
        workbook = xlsxwriter.Workbook(textfile.replace('.txt', '.xlsx'))
        worksheet = workbook.add_worksheet()
        i = 0

        for column in column_list:
            for item in range(len(column)):
                if '>' in column[item] or '<' in column[item]:
                    worksheet.write(item, i, column[item])
                else:
                    worksheet.write(item, i, float(column[item]))
            i+=1

        workbook.close()


if __name__ == '__main__':

    for textfile in textfiles:
        split_file(textfile)

    new_textfiles = [os.path.join(filepath, f) for f in os.listdir(filepath)
                    if os.path.isfile(os.path.join(filepath, f)) and '.txt' in f]
    convert_all_files(new_textfiles)
