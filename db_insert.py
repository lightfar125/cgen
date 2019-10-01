import sqlite3
import csv

conn = sqlite3.connect('ontario649.db')
print("Opened database successfully")

c = conn.cursor()
numbers = []

with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for r in reader:
        if len(r) > 0:
            numbers.append((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))

            print(f'Inserting {len(numbers)} records')
            c.executemany('INSERT INTO numbers VALUES (?,?,?,?,?,?,?,?)', numbers)
            conn.commit()
            print("Records created successfully")

# Export all entries to csv
# c.execute('SELECT * FROM numbers ORDER BY date')
# for r in c.fetchall():
#     print(f'{r[0]},{r[1]},{r[2]},{r[3]},{r[4]},{r[5]},{r[6]},{r[7]}')

conn.close()
