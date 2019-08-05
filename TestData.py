#! /usr/bin/python3
import sqlite3
#import mysql.connector
#from mysql.connector import errorcode
import random
from faker import Faker
TD = Faker('en_GB')#this can be set to other languages see docs for more info
connection = sqlite3.connect('TestData.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS customers (name text, address text, email text)''')

cursor.execute('INSERT INTO customers VALUES(:name, :address, :email)',
               {'name': TD.name(), 'address': TD.address(), 'email': TD.email()}
               )

cursor.execute('SELECT * FROM customers')

for i in cursor.execute('SELECT name, address, email FROM customers'):
    print(i)

connection.commit()

connection.close()

#var1 = input("How Many Identities should be generated? : ")
#count = (int(var1))
#class Customers:
#        def __init__(self, name, address, email):
#            self.name = name
#            self.age = random.randint(18,65)
#            self.address = address
#            self.email = email
#        def __repr__(self):
#            return 'Name: {}Age: {}Address: {},Email: {},'.format(self.name,self.age,self.address,self.email)

#customer1 = Customers(TD.name(),TD.address(),TD.email())
#for _ in range(0,count):
#    print("##########  START  ##########")
#    print(customer1)
#    print("##########   END  ###########")
#    print("")
