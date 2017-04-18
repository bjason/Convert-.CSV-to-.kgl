# csv2xml.py
# author: Yuchu LEI

import csv
import os

#input your directory here
directory = 'E:\Downloads'

for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        # print(os.path.join(directory, filename))
		csvFile = filename
		listName = os.path.splitext(csvFile)[0]
		kglFile = listName + '.kgl'

		csvData = csv.reader(open(csvFile))
		kglData = open(kglFile, 'w')
		kglData.write('<?xml version="1.0" encoding="windows-1252"?>\n')
		# there must be only one top-level tag
		kglData.write('<List ListName="' + listName + '">\n\n')

		for row in csvData:
    
			kglData.write('<File>' + "\n")
			songName = row[1]+ ' - ' + row[2]
			kglData.write('    ' + '<FileName>' \
                  + songName + '</FileName>' + "\n")
			kglData.write('</File>' + "\n\n")
            
		kglData.write('</List>' + "\n")
		kglData.close()
    else:
        continue
