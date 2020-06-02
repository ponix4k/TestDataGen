#! /usr/bin/python3
import sqlite3
import random

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

#def db_connect():
#    try:
#        connection = sqlite3.connect('TestData.db')
#        cursor = connection.cursor()
#        print("Database created and successfully connected to SQLite")
#        sql_string = "select dob from customers;"
#        cursor.execute(sql_string)
#        result = cursor.fetchall()
#        print("Query returned: ",result)
#        cursor.close()
#    except sqlite3.Error as error:
#        print("Error wile connection sqlite", error)
#    finally:
#        if (connection):
#            connection.close()
#            print("The SQLite connection is closed")

def create_data():
    connection = sqlite3.connect('TestData.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers ("Name" TEXT, "Birthdate" text, "Address" TEXT, "Email" TEXT);''')
    cursor.execute('INSERT INTO customers VALUES(:Name, :Birthdate, :Address, :Email)',{'Name': TD.name(), 'Birthdate': str(TD.date_of_birth(minimum_age=17, maximum_age=85)),
    'Address': TD.address(), 'Email': TD.email()})
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
    print("Name, Dob, Address, Email")
    cursor.execute('SELECT * FROM customers')
    for i in cursor.execute('SELECT Name, Birthdate, Address, Email FROM customers'):
        print(i)

def main():
    opt1 = input("Do you want to READ or WRITE (R/W/eXit): ")
    if opt1.upper() == 'R':
        select_data()        
    elif opt1.upper() == 'W':
        opt2 = input("Do you want to create more than one record?(Y/N/eXit): ")
        if opt2.upper() == 'Y':
            multi_create()
        elif opt2.upper() == 'N':
            create_data()
        elif opt2.upper() == 'X':
            print("Goodbye")
            exit()
        else:
            print("Invalid option please try again")
            main()
    elif opt1.upper() == 'X':
        print("Goodbye")
        exit()
    else:
        print("Invalid option please try again")
        main()

if __name__ == "__main__":
    main()
