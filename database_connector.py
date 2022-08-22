import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="Mohit Prajapat",
                               passwd="7877",
                               database="library")

mycursor = mydb.cursor()
try:
    mycursor.execute("create table books(Name varchar(30),"
                     "Author varchar(20),"
                     "istrue varchar(5))")
except Exception as e:
    pass
try:
    mycursor.execute("create table guest(user varchar(30),"
                     "book varchar(20),"
                     "status varchar(10))")
except Exception as e:
    pass
mydb.commit()