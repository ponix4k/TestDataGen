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
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (CID INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT, Contact_Number TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICEHEADER (INVHEADID INTEGER PRIMARY KEY, Customer_AccountNo TEXT, Customer_Name TEXT, Customer_Address TEXT, Contact_Number TEXT,Email TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICELINES (IVNLINE INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT, Contact_Number TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS PARTS (PID INTEGER PRIMARY KEY AUTOINCREMENT, Part_Name TEXT, Cost TEXT,BaseCurrency TEXT, QTY INTEGER);")
    cur.execute("CREATE TABLE IF NOT EXISTS PRODUCTS (PRID INTEGER PRIMARY KEY, Product_name TEXT, Product_Colour TEXT, TEXT DEFAULT '',Product_Type TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS USERS (UID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Birthdate TEXT DEFAULT '01-01-1899',Contact_Number TEXT,Email TEXT, Password TEXT, Job_Title TEXT DEFAULT 'Worker',StartDate TEXT DEFAULT '01-01-1899');")
    conn.commit()
    conn.close()
    print("Database Initalised")

def create_password(stringLength):
    chars = string.ascii_letters + string.digits + string.punctuation
    password =''.join(secrets.choice(chars) for i in range(stringLength))
    return password
### User Creation ###
def create_users(first_name,last_name,BirthDate,contact_number,email,password,Job_Title,StartDate):
    conn = sqlite3.connect("TestData.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (First_Name,Last_Name,Birthdate,Contact_Number,Email,Password,Job_Title,StartDate) Values (?,?,?,?,?,?,?,?)",
    (first_name,last_name,BirthDate,contact_number,email,password,Job_Title,StartDate))
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
        create_users(Fname,Lname,str(TD.date_of_birth(minimum_age=17, maximum_age=85)),TD.phone_number(),Email,create_password(16),TD.job(),str(TD.date_this_century()))
        i += 1

def select_users():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM Users')
    for i in cur.execute('SELECT UID,First_Name, Last_Name, Birthdate, Password, Email, Job_Title, StartDate FROM Users'):
        print(i)
    conn.close()
###
### Part Creation ###
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
    cur.execute('SELECT * FROM PARTS')
    for i in cur.execute('SELECT PAAD,First_Name, Last_Name, Birthdate, Password, Email, Job_Title, StartDate FROM Users'):
        print(i)
    conn.close()
###
### Product Creation ###
def create_product_clothes():
    specials = "'[]!~#@"
    colours = ['Red','Orange','Yellow','Green','Blue','Indigo','Violet','Black','White','Grey']
    hue = ['Light','Dark']
    types = ['T-shirt','Socks','Pants','Underwear','Jumper','Hoody']
    product = TD.words(1,types,True)
    productName = str(product)
    for char in specials:
        productName = productName.replace(char,"")
    productHue = TD.words(1,hue,True) 
    productColourSelection = TD.words(1,colours,True)
    productColour = (str(productHue)+' '+str(productColourSelection))
    for char in specials:
        productColour = productColour.replace(char,"")
    productDescription = (str(productColour)+' '+str(productName))
    for char in specials:
        productDescription = productDescription.replace(char,"")    
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO PRODUCTS (Product_name,  Product_Colour , Product_Description, Product_Type  ) VALUES (?,?,?,?)",(str(productName),  str(productColour) , str(productDescription), 'Clothes'))#Product_Type
    conn.commit()
    conn.close()
    

def multi_create_product():
    i = 0
    count = input("How many items do you want to create: ")
    while i < int(count):
        create_product_clothes()
        i += 1
    print("Records Created")

def select_products():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM PRODUCTS')
    print ('PRID  , Product_name, Product_Colour, Product_Description, Product_Type')
    for i in cur.execute('SELECT PRID, Product_name, Product_Colour, Product_Description, Product_Type FROM Products'):
        print(i)
    conn.close()
###

def main():
    specials = "'[]!~#@"
    dbinit()
    Fname = TD.first_name()
    Lname = TD.first_name()
    Domain = TD.domain_name()
    Email = Fname+'.'+Lname+'@'+Domain
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
                    #create_users()
                    #create_part()
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
                        create_users(Fname,Lname,str(TD.date_of_birth(minimum_age=17, maximum_age=85)),TD.phone_number(),Email,create_password(16),TD.job(),str(TD.date_this_century()))
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