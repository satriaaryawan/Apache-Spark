import os,glob
from shutil import copyfile

cwd = os.getcwd()
file_csv = []

for file in glob.glob('*.csv'):
    file_csv.append(file)

copyfile(file_csv[0], 'clicks_hour.csv')
combine_file=open('clicks_hour.csv','a')
file_csv.pop(0)

for i in file_csv:
    with open(i) as f:
        next(f)
        for line in f:
            combine_file.write(line)