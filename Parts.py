#! /usr/bin/python3
import sqlite3
import random
from faker import Faker
rand = random.Random()
TD = Faker('en_GB')#this can be set to other languages see docs for more info

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS PARTS (PA_ID INTEGER PRIMARY KEY AUTOINCREMENT, Part_Name TEXT, Cost TEXT,BaseCurrency TEXT,BaseCurrencySymbol TEXT, QTY INTEGER);")
    conn.commit()
    conn.close()
### Part Creation ###
def create_part():
    
    Part_Name = (TD.word()+'-'+str(TD.random_int(1,10000)))
    Cost = (TD.random_int(1,100))
    BaseCurrency = str(TD.currency_name())
    BaseCurrencySymbol = str(TD.currency_symbol())
    QTY = (TD.random_int(1,100))
    #print (Part_Name,Cost,BaseCurrency,QTY)
    conn = sqlite3.connect('TestData.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO PARTS (Part_Name,Cost,BaseCurrency,BaseCurrencySymbol,QTY) Values (?,?,?,?,?)",
               (Part_Name,Cost,BaseCurrency,BaseCurrencySymbol,QTY))
    conn.commit()
    conn.close()

def multi_create_parts():
    i = 0 
    count = input("How many names would you like to generate?: ")
    while i < int(count):
        create_part()
        i += 1

def select_parts():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM PARTS')
    for i in cur.execute('SELECT PA_ID,Part_Name,Cost,BaseCurrency,BaseCurrencySymbol,QTY FROM Parts'):
        print(i)
    conn.close()


