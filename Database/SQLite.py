import os

import sqlite3


os.chdir('./Database')

conn = sqlite3.connect('test_sqlite.db')
# conn = sqlite3.connect(':memory:')

curs = conn.cursor()

# .tables
#curs.execute(
#    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
# )
#conn.commit()

# SELECT * FROM persons;
#curs.execute(
#    'INSERT INTO persons(name) values("Mike")'
#)
#conn.commit()

#curs.execute('SELECT * FROM persons')
#print(curs.fetchall())

#curs.execute(
#    'INSERT INTO persons(name) values("Nancy")'
#)
#curs.execute(
#    'INSERT INTO persons(name) values("Jun")'
#)
#conn.commit()
#curs.execute('SELECT * FROM persons')
#print(curs.fetchall())

#curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
#conn.commit()


curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.close()
conn.close()




'''
sqlite3 xxx.db
commitしないとDBには反映されない。
inmemory databaseで使いたい時はsqlite3.connect(':memory:')を使う

'''