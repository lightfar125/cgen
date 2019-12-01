# Process scraped csv into correct format

import csv
from pathlib import Path
from dateutil import parser

path = Path()
data_folder = 'data'
infile = path / data_folder / '2019.csv'
outfile = path / data_folder / '2019_formatted.csv'

with open(infile, 'r') as in_csv:
    reader = csv.reader(in_csv, delimiter=',')

    with open(outfile, 'w', newline='') as out_csv:
        writer = csv.writer(out_csv, delimiter=',')

        for r in reversed(list(reader)):
            dt = parser.parse(r[0])
            newrow = [dt.date(), r[1], r[2], r[3], r[4], r[5], r[6], r[7]]
            writer.writerow(newrow)
