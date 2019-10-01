import sqlite3


conn = sqlite3.connect('ontario649.db')
print("Opened database successfully")

c = conn.cursor()

numbers = {}
for i in range(1, 50):
    numbers[i] = 0

c.execute("SELECT * FROM numbers WHERE date > '2019-07-01'")
for row in c.fetchall():
    print(f'adding numbers for {row[0]}')
    for item in row:
        if type(item) == int:
            numbers[item] += 1
            print(f'adding 1 to {item}. total: {numbers[item]}')

print(sorted(numbers.items(), key = lambda kv:(kv[1], kv[0])))

conn.close()
