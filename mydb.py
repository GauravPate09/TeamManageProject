import mysql.connector

dataBase = mysql.connector.connect(

    host='localhost',
    user = 'root',
    password ='admin123'
)
# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE sys_new")