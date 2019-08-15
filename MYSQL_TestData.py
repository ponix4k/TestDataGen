#! /usr/bin/python3
import random
import mysql.connector
from mysql.connector import errorcode
from faker import Faker
TD = Faker('en_GB')#this can be set to other languages see docs for more info

mydb = mysql.connector.connect(option_files='Connection.conf')
print("Succsess Conection ID:", mydb.connection_id)
mycursor = mydb.cursor()
mycursor.execute("Show tables")
mydb.close()
