import sqlite3
a = input()
con = sqlite3.connect(a)
cur = con.cursor()
result = cur.execute(f"""SELECT title FROM films
    WHERE title like '%Астерикс%' AND NOT LIKE '%Обеликс%'""").fetchall()
for elem in result:
    print(elem[0])
con.close()