#! /usr/bin/python3
import sqlite3
import random
import string


from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def create_password(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def create_users():
    connection = sqlite3.connect('TestData.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Users ("Name" TEXT, "Birthdate" text, "Password" TEXT, "Email" TEXT);')
    cursor.execute('INSERT INTO Users VALUES(:Name, :Birthdate, :Password, :Email)',
    {'Name': TD.name(), 'Birthdate': str(TD.date_of_birth(minimum_age=17, maximum_age=85)),'Password': create_password(10), 'Email': TD.email()})
    select_users()
    connection.commit()
    connection.close()

def multi_create_users():
    i = 0 
    count = input("How many names would you like to generate?: ")
    while i < int(count):
        create_users()
        i += 1

def create_customers():
    connection = sqlite3.connect('TestData.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS CUSTOMERS ("Name" TEXT, "Birthdate" text, "Address" TEXT, "Email" TEXT);')
    cursor.execute('INSERT INTO CUSTOMERS VALUES(:Name, :Birthdate, :Address, :Email)',{'Name': TD.name(), 'Birthdate': str(TD.date_of_birth(minimum_age=17, maximum_age=85))
    ,'Address': TD.address(), 'Email': TD.email()})
    select_customers()
    connection.commit()
    connection.close()

def multi_create_customers():
    i = 0 
    count = input("How many names would you like to generate?: ")
    while i < int(count):
        create_customers()
        i += 1

def select_users():
    connection = sqlite3.connect('TestData.db')
    cursor = connection.cursor()
    print ("############################")
    print ("########### Users ##########")
    print ("############################")
    print("Name, Dob, Password, Email")
    cursor.execute('SELECT * FROM Users')
    for i in cursor.execute('SELECT Name, Birthdate, Password, Email FROM Users'):
        print(i)
    connection.close()

def select_customers():
    connection = sqlite3.connect('TestData.db')
    cursor = connection.cursor()
    print ("############################")
    print ("######## Customers #########")
    print ("############################")
    cursor.execute('SELECT * FROM CUSTOMERS')
    for i in cursor.execute('SELECT Name, Birthdate, Address, Email FROM CUSTOMERS'):
        print(i)
    connection.close()

def select_all_data():
    select_users()
    select_customers()
   

def main():
    opt1 = input("Do you want to READ or WRITE (R/W/eXit): ")
    if opt1.upper() == 'R':
        opt1a = input("What data would you like to read ? Customers ,User ,All(C,U,A): ")
        if opt1a.upper() == 'C':
            select_customers()
        elif opt1a.upper() == 'U':
            print ("Users")
        #elif opt1a.upper() == 'P':
        #    print ("Parts")
        elif opt1a.upper() == 'A':
            print ("ALL")
        else:
            print ("Invalid selection")
    elif opt1.upper() == 'W':
            opt2 = input("What data would you like to Create ? Customers ,Users(C,U,): ")
            if opt2.upper() == 'C':
                    opt2a = input("Do you want to create more than one record?(Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_customers()
                    elif opt2a.upper() == 'N':
                        create_customers()
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()

            elif opt2.upper() == 'U':
                    opt2a = input("Do you want to create more than one record?(Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_users()
                    elif opt2a.upper() == 'N':
                        create_users()
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()

            
        #elif opt2.upper() == 'P':
        #    print ("Parts")
            else:
                print ("Invalid selection")

    elif opt1.upper() == 'X':
        print("Goodbye")
        exit()
    else:
        print("Invalid option please try again")
    main()

if __name__ == "__main__":
    main()
