#! /usr/bin/python3
import sqlite3
import string
import secrets
import datetime

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS PARTS (PID INTEGER PRIMARY KEY AUTOINCREMENT, Part_Name TEXT, Cost TEXT,BaseCurrency TEXT, QTY INTEGER);")
    cur.execute("CREATE TABLE IF NOT EXISTS USERS (UID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Birthdate TEXT DEFAULT '01-01-1899',Email TEXT, Password TEXT, Job_Title TEXT DEFAULT 'Worker',StartDate TEXT DEFAULT '01-01-1899');")
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (CID INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT);")
    conn.commit()
    conn.close()
    print("DataBase Initalised")

def create_password(stringLength):
    chars = string.ascii_letters + string.digits + string.punctuation
    password =''.join(secrets.choice(chars) for i in range(stringLength))
    return password

def create_users(first_name,last_name,BirthDate,email,password,Job_Title,StartDate):
    conn = sqlite3.connect("TestData.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (First_Name,Last_Name,Birthdate,Email,Password,Job_Title,StartDate) Values (?,?,?,?,?,?,?)",
    (first_name,last_name,BirthDate,email,password,Job_Title,StartDate))
    conn.commit()
    print ("Data Added")
    conn.close()

def multi_create_users():
    i = 0 
    count = input("How many names would you like to generate?: ")
    while i < int(count):
        Fname = TD.first_name()
        Lname = TD.first_name()
        Domain = TD.domain_name()
        Email = Fname+'.'+Lname+'@'+Domain
        create_users(Fname,Lname,str(TD.date_of_birth(minimum_age=17, maximum_age=85)),Email,create_password(16),TD.job(),str(TD.date_this_century()))
        i += 1

def select_users():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM Users')
    for i in cur.execute('SELECT UID,First_Name, Last_Name, Birthdate, Password, Email, Job_Title, StartDate FROM Users'):
        print(i)
    conn.close()

def create_part(Part_Name,Cost,BaseCurrency,QTY):
    conn = sqlite3.connect('TestData.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO PARTS (Part_Name,Cost,BaseCurrency,QTY) Values (?,?,?,?)",(Part_Name,Cost,BaseCurrency,QTY))
    conn.commit()
    conn.close()

def multi_create_parts():
    i = 0 
    count = input("How many names would you like to generate?: ")
    while i < int(count):
        create_part(TD.word()+'-'+str(TD.random_int(1,10000)),TD.random_int(1,100),'£',TD.random_int(1,100))
        i += 1

def select_parts():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("select * from PARTS")
    rows=cur.fetchall()
    conn.close()
    return rows

def main():
    Fname = TD.first_name()
    Lname = TD.first_name()
    Domain = TD.domain_name()
    Email = Fname+'.'+Lname+'@'+Domain
    opt1 = input("Do you want to READ or WRITE (R/W/eXit): ")
    if opt1.upper() == 'R':
        opt1a = input("What data would you like to read ? Customers ,User ,All (C,U,A): ")
        if opt1a.upper() == 'C':
            print("select customers")
            #select_customers()
        elif opt1a.upper() == 'U':
            select_users()
        elif opt1a.upper() == 'P':
            select_parts()
        elif opt1a.upper() == 'A':
            select_all_data()
        else:
            print ("Invalid selection")
    elif opt1.upper() == 'W':
            opt2 = input("What data would you like to Create ? Customers ,Users, Parts (C,U,P): ")
            if opt2.upper() == 'C':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        #multi_create_users()
                        pass
                    elif opt2a.upper() == 'N':
                        #create_customers()
                        pass
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()

            elif opt2.upper() == 'U':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_users()
                    elif opt2a.upper() == 'N':
                        create_users(Fname,Lname,str(TD.date_of_birth(minimum_age=17, maximum_age=85)),Email,create_password(16),TD.job(),str(TD.date_this_century()))
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()
            elif opt2.upper() == 'P':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_parts()
                    elif opt2a.upper() == 'N':
                        create_part()
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()
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