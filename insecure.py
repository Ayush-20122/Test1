import mysql.connector
db = mysql.connector.connect
#Bad Practice. Avoid this! This is just for learning.
(host="localhost", user="newuser", passwd="pass", db="sample")
cur = db.cursor()
name = raw_input('Enter Name: ')
cur.execute("SELECT * FROM sample_data WHERE Name = '%s';" % name) for row in cur.fetchall(): print(row)
db.close()
