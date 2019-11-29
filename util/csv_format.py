# Process csv file to expand six integer columns into 52 binary
# columns, with a 1 placed in each column that corresponded to
# a number found in the input columns

import csv
from pathlib import Path

path = Path()
data_folder = 'data'
infile = path / data_folder / 'numbers_raw.csv'
outfile = path / data_folder / 'numbers.csv'

with open(infile, 'r') as in_csv:
    reader = csv.reader(in_csv, delimiter=',')

    with open(outfile, 'w', newline='') as out_csv:
        writer = csv.writer(out_csv, delimiter=',')

        for row in reader:
            # create array of 52 zeroes
            new_row = [0 for i in range(52)]
            # fill first three slots with year, month, day
            for idx, item in enumerate(row[:3]):
                new_row[idx] = int(item)
            # fill in 1 where ball number = column number
            for item in row[3:]:
                new_row[int(item) + 2] = 1

            writer.writerow(new_row)
