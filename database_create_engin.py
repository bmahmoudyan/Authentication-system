from info import username, password, host
import mysql.connector


db_connector = mysql.connector.connect(
    host=host, user=username, passwd=password,)

my_cursor = db_connector.cursor()

my_cursor.execute("CREATE DATABASE mysqldb")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

# my_cursor.close()
print('All Done!')
