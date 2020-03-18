import mysql.connector
'''
#conn = mysql.connector.connect(host="127.0.0.1", user="root", password="")
conn = mysql.connector.connect(host="127.0.0.1")
cursor = conn.cursor()
cursor.execute(
    'CREATE DATABASE test_mysql_database2'
)
cursor.close()
conn.close()
'''

conn = mysql.connector.connect(host="127.0.0.1", database="test_mysql_database", user="root")
cursor = conn.cursor()
#curosr.execute(
#    'CREATE TABLE persons(id int NOT NULL AUTO_INCREMENT, name varchar(14) NOT NULL, PRIMARY KEY(id))'
#)

cursor.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.close()
conn.close()

'''
brew services start mysql
brew services stop mysql
brew services list

mysql -u root
show databases;
use test_mysql_database;


brew install mysql-client
https://pypi.org/project/mysqlclient/
https://basicincome30.com/python3-mysql-connector
'''