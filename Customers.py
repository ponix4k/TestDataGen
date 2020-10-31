import secrets
import string
import sqlite3

from faker import Faker

TD = Faker('en_GB')

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (CID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Birthdate TEXT DEFAULT '01-01-1899', Address TEXT DEFAULT '123 WISHING LANE', Contact_Number TEXT, Email TEXT, Password TEXT);")
    conn.commit()
    conn.close()
    

def create_password(stringLength):
    chars = string.ascii_letters + string.digits + string.punctuation
    Password =''.join(secrets.choice(chars) for i in range(stringLength))
    return Password

def create_customer(init_db = True ):
    Password = create_password(16)
    Fname = TD.first_name()
    Lname = TD.first_name()
    Domain = TD.domain_name()
    Email = Fname+'.'+Lname+'@'+Domain
    Address = TD.address()
    ContactNumber = TD.phone_number()
    BirthDate = TD.date_of_birth(minimum_age=17, maximum_age=85)
    conn = sqlite3.connect("TestData.db")
    cur = conn.cursor()
    if (init_db): ## only need to initialise it once
        dbinit()
    
    cur.execute("INSERT INTO CUSTOMERS (First_Name, Last_Name, Birthdate, Address, Contact_Number, Email, Password) Values (?,?,?,?,?,?,?)",
    (Fname, Lname, BirthDate, Address, ContactNumber, Email, Password,))
    conn.commit()
    conn.close()

def multi_create_customers(count):
    i = 0  
    while i < int(count):
        Fname = TD.first_name()
        Lname = TD.first_name()
        Domain = TD.domain_name()
        Email = Fname+'.'+Lname+'@'+Domain
        Address = TD.address()
        BirthDate = TD.date_of_birth(minimum_age=17, maximum_age=85)
        create_customer(i == 0)
        i += 1

def select_customers():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM CUSTOMERS')
    for i in cur.execute('SELECT CID, First_Name, Last_Name, Birthdate, Address, Contact_Number, Email, Password FROM CUSTOMERS'):
        print(i)
    conn.close()

