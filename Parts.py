#! /usr/bin/python3
import sqlite3
from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info


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