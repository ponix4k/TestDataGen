#! /usr/bin/python3
import sqlite3
import random

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def db_connect():
    try:
        connection = sqlite3.connect('TestData.db')
        cursor = connection.cursor()
        print("Database created and successfully connected to SQLite")
        sql_string = "select * from customers;"
        cursor.execute(sql_string)
        result = cursor.fetchall()
        print("Query returned: ",result)
        cursor.close()
    except sqlite3.Error as error:
        print("Error wile connection sqlite", error)
    finally:
        if (connection):
            connection.close()
            print("The SQLite connection is closed")

def create_data():
    connection = sqlite3.connect('TestData.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (name text, address text, email text)''')
    cursor.execute('INSERT INTO customers VALUES(:name, :address, :email)',{'name': TD.name(), 'address': TD.address(), 'email': TD.email()})
    print("Single Record Created")
    select_data()
    connection.commit()
    connection.close()

def multi_create():
    i = 0 
    count = input("How many names would you like to generate?: ")
    while i < int(count):
        create_data()
        i += 1
    select_data()

def select_data():
    connection = sqlite3.connect('TestData.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM customers')
    for i in cursor.execute('SELECT name, address, email FROM customers'):
        print(i)


def main():
    opt = input("Do you want to create more than one record?(Y/N): ")
    if opt.upper() == 'Y':
        multi_create()
    else:
        create_data()

if __name__ == "__main__":
    main()