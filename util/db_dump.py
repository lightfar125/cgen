# Script to dump contents of database into csv file for
# processing with numpy

import sqlite3

conn = sqlite3.connect('ontario649.db')
c = conn.cursor()

c.execute("SELECT * FROM numbers")

# Output all records for redirection to csv
for row in c.fetchall():
    date = row[0]
    year = date[:date.find('-')]
    month = date[date.find('-') + 1:date.rfind('-')]
    day = date[date.rfind('-') + 1:]
    print(f'{year},{month},{day},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]}')

conn.close()
