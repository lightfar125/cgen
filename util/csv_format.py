import csv
from datetime import date

infile = 'input.csv'
outfile = 'numbers.csv'

with open(infile, 'r') as incsv:
    reader = csv.reader(incsv, delimiter=',')

    with open(outfile, 'w') as outcsv:
        writer = csv.writer(outcsv, delimiter=',')

        for row in reader:
            c = row[0]
            year = c[c.rfind('/') + 1:]
            year = year[-2:]
            if int(year) < 50:
                year = '20' + str(year)
            else:
                year = '19' + str(year)
            month = int(c[:c.find('/')])
            day = int(c[c.find('/') + 1:c.rfind('/')])
            d = date(int(year), month, day)
            row[0] = d
            writer.writerow(row)
