#! /usr/bin/python3
import sqlite3
import string
from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def connect():
    conn = sqlite3.connect('TestData.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS PARTS (PID INTEGER PRIMARY KEY AUTOINCREMENT, Part_Name TEXT, Cost TEXT,BaseCurrency TEXT, QTY INTEGER);")
    cur.execute("CREATE TABLE IF NOT EXISTS USERS (UID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (CID INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT);")
    conn.commit()
    conn.close()

def insert_part(Part_Name,Cost,BaseCurrency,QTY):
    conn = sqlite3.connect('TestData.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO PARTS (Part_Name,Cost,BaseCurrency,QTY) Values (?,?,?,?)",(Part_Name,Cost,BaseCurrency,QTY))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("select * from PARTS")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
insert_part(TD.word()+'-'+str(TD.random_int(1,10000)),TD.random_int(1,100),'£',TD.random_int(1,100))

print(view())



#def create_part():
#    
#    cursor = connection.cursor()
#    partName = (TD.word()+'-'+str(TD.random_int(1,10000)))
#    cursor.execute('CREATE TABLE IF NOT EXISTS PARTS ("PID" INTEGER, "Part_Name" TEXT, "Cost" real,"BaseCurrency" TEXT, "QTY" INTEGER);')
#    cursor.execute('INSERT INTO PARTS VALUES(:PID, :Part_Name, :Cost, :BaseCurrency, :QTY)',{'Part_Name': partName,'BaseCurrency':'£', 'Cost':TD.random_int(1,100)
#    ,'QTY': TD.random_int(1,100)})
#    connection.commit()
#    connection.close()#

#def multi_create_parts():
#    i = 0 
#    count = input("How many parts would you like to generate?: ")
#    while i < int(count):
#        create_part()
#        i += 1##

#def select_parts():
#    connection = sqlite3.connect('TestData.db')
#    cursor = connection.cursor()
#    print ("############################")
#    print ("########## PARTS ###########")
#    print ("############################")
#    cursor.execute('SELECT * FROM PARTS')
#    for i in cursor.execute('SELECT PID, Part_Name, Cost, BaseCurrency, QTY FROM PARTS'):
#        print(i)
#    connection.close()
#    print ("#########################")#

#def main():
#    opt1 = input("Do you want to READ or WRITE (R/W/eXit): ")
#    if opt1.upper() == 'R':
#        select_parts()
#    elif opt1.upper() == 'W':
#        opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
#        if opt2a.upper() == 'Y':
#            multi_create_parts()
#            select_parts()
#        elif opt2a.upper() == 'N':
#            create_part()
#    elif opt1.upper() == 'X':
#        exit()

#if __name__ == "__main__":
#    main()