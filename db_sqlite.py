import sqlite3

con = sqlite3.connect('my-test.db')
# cur = con.cursor()

con.execute("""
    CREATE TABLE IF NOT EXISTS USER (
        id INT NOT NULL PRIMARY KEY,
        name TEXT,
        bank INTEGER,
        wins INTEGER,
        loss INTEGER
    );
""")

# sql = 'INSERT INTO USER (id, name, bank, wins, loss) values(?, ?, ?, ?, ?)'
# data = [
#     (720893757, 'Павел', 21, 0, 0),
# ]

# with con:
# con.executemany(sql, data)

# with con:
#   con.execute("UPDATE USER SET loss=4 WHERE id=720893757")

# with con:
data = con.execute("SELECT * FROM USER")
for row in data:
    print(row)