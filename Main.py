#! /usr/bin/python3
from Users import (create_user, multi_create_users, select_users)
from Customers import(create_customer, multi_create_customers, select_customers)
from Parts import (create_part, multi_create_parts, select_parts)
from Products import (create_product_clothes, multi_create_product_clothes, select_products)
import sqlite3
import string

import datetime

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS USERS (UID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Birthdate TEXT DEFAULT '01-01-1899',Contact_Number TEXT,Email TEXT, Password TEXT, Job_Title TEXT DEFAULT 'Worker',StartDate TEXT DEFAULT '01-01-1899');")
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (CID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Birthdate TEXT DEFAULT '01-01-1899', Address TEXT DEFAULT '123 WISHING LANE', Contact_Number TEXT, Email TEXT, Password TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICEHEADER (INVHEADID INTEGER PRIMARY KEY, Customer_AccountNo TEXT, Customer_Name TEXT, Customer_Address TEXT, Contact_Number TEXT,Email TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICELINES (IVNLINE INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT, Contact_Number TEXT);")
        
    print("Database Initalised")

def print_title(title):
        print("################")
        print(title)
        print("################")

def main():
    specials = "'[]!~#@"
    opt1 = input("Do you want to READ or WRITE (R/W/eXit): ")
    if opt1.upper() == 'R':
        opt1a = input("What data would you like to read ? (C)ustomers, (U)ser, (PR)oducts, (Pa)rts, All (C/U/PA/PR): ")
        if opt1a.upper() == 'C':
            print("select customers")
            select_customers()
        elif opt1a.upper() == 'U':
            select_users()
        elif opt1a.upper() == 'PA':
            select_parts()
        elif opt1a.upper() == 'PR':
            select_products()
        elif opt1a.upper() == 'A':
            dbinit()
            print_title("Customers")
            select_customers()
            print_title("Users")
            select_users()
                       
            print_title("Parts")
            select_parts()
            
            print_title("Products")
            select_products()
                        
            print_title("All info seleted")
                        
        else:
            print ("Invalid selection")
    elif opt1.upper() == 'W':
            opt2 = input("What data would you like to Create? (C)ustomers, (U)ser, (PR)oducts, (PA)rts ,(A)ll: ")
            if opt2.upper() == 'A':
                opt2a = input("Do you want to create multiple records? ")
                if opt2a.upper() == 'Y':
                    multi_create_product_clothes()
                    multi_create_users(input("How many names would you like to generate?: "))
                    multi_create_parts(input("How many parts would you like to generate?: "))
                elif opt2a.upper() == 'N':
                    create_product_clothes()
                else:
                    print("Invalid selecton")

            elif opt2.upper() == 'C':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_customers(input("How many customers would you like to generate?: "))
                        pass
                    elif opt2a.upper() == 'N':
                        create_customers()
                        pass
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()

            elif opt2.upper() == 'U':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_users(input("How many users would you like to generate?: "))
                    elif opt2a.upper() == 'N':
                        create_user()
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()
            elif opt2.upper() == 'PA':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_parts(input("How many parts would you like to generate?: "))
                    elif opt2a.upper() == 'N':
                        create_part()
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()
            elif opt2.upper() == 'PR':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_product_clothes(input("How many clothes would you like to generate?: "))
                    elif opt2a.upper() == 'N':
                        create_product_clothes()
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