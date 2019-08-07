#! /usr/bin/python3
import sqlite3
import random

from faker import Faker
TD = Faker('en_GB')#this can be set to other languages see docs for more info
connection = sqlite3.connect('TestData.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS customers (name text, address text, email text)''')

cursor.execute('INSERT INTO customers VALUES(:name, :address, :email)',
               {'name': TD.name(), 'address': TD.address(), 'email': TD.email()
                }
               )

cursor.execute('SELECT * FROM customers')

for i in cursor.execute('SELECT name, address, email FROM customers'):
    print(i)

connection.commit()

connection.close()
