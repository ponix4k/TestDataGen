#!/usr/bin/python3
from Users import (create_users,multi_create_users,select_users)
from Parts import (create_part,multi_create_parts,select_parts)
#from Products import ()
import sqlite3
import string

import datetime

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (CID INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT, Contact_Number TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICEHEADER (INVHEADID INTEGER PRIMARY KEY, Customer_AccountNo TEXT, Customer_Name TEXT, Customer_Address TEXT, Contact_Number TEXT,Email TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICELINES (IVNLINE INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT, Contact_Number TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS PARTS (PID INTEGER PRIMARY KEY AUTOINCREMENT, Part_Name TEXT, Cost TEXT,BaseCurrency TEXT, QTY INTEGER);")
    cur.execute("CREATE TABLE IF NOT EXISTS PRODUCTS (PRID INTEGER PRIMARY KEY, Product_name TEXT, Product_Colour TEXT, TEXT DEFAULT '',Product_Type TEXT);")
    conn.commit()
    conn.close()
    print("Database Initalised1")

def main():
    specials = "'[]!~#@"
    dbinit()
    opt1 = input("Do you want to READ or WRITE (R/W/eXit): ")
    if opt1.upper() == 'R':
        opt1a = input("What data would you like to read ? (C)ustomers ,(U)ser, (PR)oducts, (Pa)rts ,All (C,U,PA,PR): ")
        if opt1a.upper() == 'C':
            print("select customers")
            #select_customers()
        elif opt1a.upper() == 'U':
            select_users()
        elif opt1a.upper() == 'PA':
            select_parts()
        elif opt1a.upper() == 'PR':
            select_products()
        else:
            print ("Invalid selection")
    elif opt1.upper() == 'W':
            opt2 = input("What data would you like to Create ? (C)ustomers ,(U)ser, (PR)oducts, (PA)rts ,(A)ll : ")
            if opt2.upper() == 'A':
                opt2a = input("Do you want to create multiple records ? :")
                if opt2a.upper() == 'Y':
                    multi_create_product()
                    multi_create_users()
                    multi_create_parts()
                elif opt2a.upper() == 'N':
                    create_product_clothes()
                else:
                    print("invalid selecton")

            elif opt2.upper() == 'C':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        #multi_create_customers()
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
                        create_users()
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()
            elif opt2.upper() == 'PA':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_parts()
                    elif opt2a.upper() == 'N':
                        print("PARTS CREATION")
                        #create_part()
                    elif opt2a.upper() == 'X':
                        print("Goodbye")
                        exit()
            elif opt2.upper() == 'PR':
                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
                    if opt2a.upper() == 'Y':
                        multi_create_product()
                    elif opt2a.upper() == 'N':
                        print("PARTS CREATION")
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