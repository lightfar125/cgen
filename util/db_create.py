# Script to setup the database + table

import sqlite3

conn = sqlite3.connect('ontario649.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE numbers(
        date            TEXT    PRIMARY KEY NOT NULL,
        no1             INT     NOT NULL,
        no2             INT     NOT NULL,
        no3             INT     NOT NULL,
        no4             INT     NOT NULL,
        no5             INT     NOT NULL,
        no6             INT     NOT NULL,
        bonus           INT     NOT NULL);''')

print("Table created successfully")

conn.close()
