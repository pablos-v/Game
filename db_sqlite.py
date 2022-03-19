import sqlite3


con = sqlite3.connect('Game/matches.db', check_same_thread=False)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS USER (
            id INT PRIMARY KEY,
            name TEXT,
            bank INT,
            wins INT,
            loss INT
        );
    """)


def adduser(data):
    sql = 'INSERT INTO USER (id, name, bank, wins, loss) values(?, ?, ?, ?, ?)'
    with con:
        con.execute(sql, data)


def winloss(wl, ID):
    what = "wins" if wl else "loss"
    n = ask(what, ID) + 1
    with con:
        con.execute(f"UPDATE USER SET {what}={n} WHERE id={ID}") # TODO con.execute(f"UPDATE USER SET {what}={ask(what, ID)+1}, bank=21 WHERE id={ID}")
        con.execute(f"UPDATE USER SET bank=21 WHERE id={ID}")


def edit_bank(ID, amount):
    what = 'bank'
    with con:
        con.execute(f"UPDATE USER SET bank={ask(what, ID)-amount} WHERE id={ID}")

# список всех ID
def idlist():
    return [i[0] for i in con.execute("SELECT id FROM USER").fetchall()]

# запрос к столбцу БД
def ask(what, ID):
    return con.execute(f"SELECT {what} FROM USER WHERE id={ID}").fetchone()[0]

# d1 = (720893757, 'Павел', 21, 0, 0)
# d2 = (4444, 'Павел', 21, 0, 0)
# d3 = (555, 'Павел', 21, 0, 0)
# adduser(d1)
# adduser(d2)
# adduser(d3)
# data = con.execute("SELECT * FROM USER")
# for row in data:
#     print(row)

# print(idlist())