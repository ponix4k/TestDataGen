#! /usr/bin/python3
from faker import Faker
import sqlite3

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS PRODUCTS (PR_ID INTEGER PRIMARY KEY, Product_name TEXT, Product_Colour TEXT, Product_Description TEXT DEFAULT '',Product_Type TEXT);")
    conn.commit()
    conn.close()
### Product Creation ###
def create_product_clothes():
    dbinit()
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

def multi_create_product_clothes():
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
    print ('PR_ID  , Product_name, Product_Colour, Product_Description, Product_Type')
    for i in cur.execute('SELECT PR_ID, Product_name, Product_Colour, Product_Description, Product_Type FROM Products'):
        print(i)
    conn.close()