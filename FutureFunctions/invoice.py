#! /usr/bin/python3
import sqlite3
import string
import secrets
import datetime

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def create_invoice_header(invRecNo,first_name,last_name,email):
    print("invRecNo,first_name,  last_name, email")
    print(first_name,last_name,email)

def create_invoice_lines(invHeadRecNo,Linecount):
    i = 0 
    print (Linecount)
    print (i)
    while i < (Linecount):
        print ("line "+str(i)+" added")
        #create_line()
        i += 1

    

def create_invoice():
    HeadRecNo = (TD.random_int(100))
    Fname = TD.first_name()
    Lname = TD.last_name()
    Company = TD.domain_name()
    Email = Fname+'.'+Lname+'@'+Company
    Linecount = TD.random_int(1-10)
    create_invoice_header(HeadRecNo,Fname,Lname,Email)
    create_invoice_line(HeadRecNo)

create_invoice_lines(1,5)


#Fname = TD.first_name()
#Lname = TD.first_name()
#Domain = TD.domain_name()
#Email = Fname+'.'+Lname+'@'+Domain
#create_invoice(Fname,Lname,Email)