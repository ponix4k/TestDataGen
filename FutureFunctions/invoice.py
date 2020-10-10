import sqlite3
import string
import secrets
import datetime

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICEHEADER (INVHEADID INTEGER PRIMARY KEY, Customer_AccountNo TEXT, Customer_Name TEXT, Customer_Address TEXT, Contact_Number TEXT,Email TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS INVOICELINES (IVNLINEID INTEGER PRIMARY KEY,  Product_name TEXT, Colour TEXT, Cost INT, QTY INT);")
    conn.commit()
    conn.close()
    print("Database Initalised")

def create_invoice_header(invRecNo,Customer_AccountNo,Customer_Name,Customer_Address,Contact_Number,Email):
    #print("invRecNo,custAccountNo,customerName,customerAddress,contactNo,Email")
    conn = sqlite3.connect('TestData.db')
    cur=conn.cursor()
    #cur.execute("SELECT INVHEADID FROM INVOICEHEADER ORDER BY INVHEADHEADER DESC ")
    #InvoiceNo =cur.fetchone()[0]
    cur.execute("INSERT INTO INVOICEHEADER (Customer_AccountNo,Customer_Name,Customer_Address,Contact_Number,Email) VALUES (?,?,?,?,?)",(Customer_AccountNo,Customer_Name,Customer_Address,Contact_Number,Email))
    conn.commit()
    conn.close()
    print(str(InvoiceNo))
    print("Records Updated ")

def create_line():
    specials = "(),'[]!~#@"
    #PRID,productDesctiption,cost,qty):
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    PRID = TD.random_int(1,10)

    def get_description(PRID):
        cur=conn.cursor()
        for result in cur.execute(('SELECT Product_Description FROM PRODUCTS WHERE PRID = ?'),str(PRID)):
            return result   #  return result
    Desctiption =  (get_description(PRID))
    #stip specials
    productDesctiption = str(Desctiption)
    for char in specials:
        productDesctiption = productDesctiption.replace(char,"")
    cost = TD.random_int(1,10)
    qty = TD.random_int(1,10)
    print (PRID,productDesctiption,cost,qty)
    
def create_invoice_lines(invHeadRecNo,Linecount):
    i = 0
    while i < (Linecount):
        create_line()
        i += 1

def create_invoice():
    HeadRecNo = (TD.random_int(100))
    Fname = TD.first_name()
    Lname = TD.last_name()
    Linecount = TD.random_int(1,10)
    CompanyName = TD.domain_word()
    CompanyAddress = TD.address()
    CompanyEmail = 'Accounts@'+CompanyName+'.'+TD.tld()
    CompanyContactEmail = Fname+'.'+Lname+'@'+CompanyName+TD.tld()
    CompanyAccountNo = CompanyName[slice(0,4)]+str(TD.random_int(100,1000))
    ContactNo = TD.phone_number()
    create_invoice_header(HeadRecNo,CompanyAccountNo,CompanyName,CompanyAddress,ContactNo,CompanyEmail)
    create_invoice_lines(HeadRecNo,Linecount)

def select_invoice_headers():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM INVOICEHEADER')
    for result in cur.execute('SELECT * FROM INVOICEHEADER'):
        print(result)
    conn.close()

def get_description(PRID):
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    for result in cur.execute(('SELECT Product_Description FROM PRODUCTS WHERE PRID = ?'),str(PRID)):
        return result
        description = result
    print (description)

def main():
    #PRID = TD.random_int(1,10)
    dbinit()
    create_invoice()
    #create_line()
    #select_invoice_headers()
    #get_description(PRID)
    

if __name__ == "__main__":
    main()