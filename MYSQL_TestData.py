#! /usr/bin/python3
import random
import mysql.connector
from mysql.connector import errorcode
from faker import Faker
TD = Faker('en_GB')#this can be set to other languages see docs for more info

mydb = mysql.connector.connect(option_files='Connection.conf')
print("Succsess Conection ID:", mydb.connection_id)
mycursor = mydb.cursor()

Sql1 = """
INSERT INTO `Customers`(`Name`, `Email`, `Age`, `Phone`) 
VALUES ("""+TD.firstname()+""","""+TD.email()+""",18,"""+TD.phone_number()+""")
"""
mycursor.execute(Sql1)

Sql2 = """
select * from Customers
"""
mycursor.execute(Sql2)

#iterate over resultss
for row in mycursor:
   print(row)

mycursor.close()
mydb.close()