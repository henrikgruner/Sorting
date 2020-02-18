
import csv
import unicodecsv

mydata = []
with open('numbers.csv', 'rb') as f_input:
    input_file2 = unicodecsv.reader(f_input, encoding='utf-8-sig')
    for row in input_file2:
        if(len(row) == 1):
            mydata.append(row[0])

mydata = [int(i) for i in mydata]
NUMBERS = mydata
