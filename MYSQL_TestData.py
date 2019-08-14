#! /usr/bin/python3
import random
import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(host='localhost',user='store',
                               password='store',database='store')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    mydb.close()

mycursor = mydb.cursor()

mycursor.execute("select * from customers")

from faker import Faker
TD = Faker('en_GB')#this can be set to other languages see docs for more info
