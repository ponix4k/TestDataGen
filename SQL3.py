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
    cur.execute("CREATE TABLE IF NOT EXISTS PARTS (PID INTEGER PRIMARY KEY AUTOINCREMENT, Part_Name TEXT, Cost TEXT,BaseCurrency TEXT, QTY INTEGER);")
    cur.execute("CREATE TABLE IF NOT EXISTS USERS (UID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Birthdate TEXT DEFAULT '01-01-1899',Email TEXT, Password TEXT, Job_Title TEXT DEFAULT 'Worker',StartDate TEXT DEFAULT '01-01-1899');")
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (CID INTEGER PRIMARY KEY,  First_Name TEXT, Last_Name TEXT);")
    conn.commit()
    conn.close()
    print("DataBase Initalised")

def create_password(stringLength):
    chars = string.ascii_letters + string.digits + string.punctuation
    password =''.join(secrets.choice(chars) for i in range(stringLength))
    return password

class Person:
    def __init__(self,first_name,last_name,domain_name,birthDate):
        self.first_name = first_name,
        self.last_name = last_name,
        self.domain_name = domain_name,
        self.birthDate = birthDate

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def email(self):
        return '{}.{}@{}'.format(self.first_name, self.last_name, self.domain_name)
        print(self.Email)

    def DOB(self):
        return '{}'.format(self.birthDate)

def create_users(first_name,last_name,DOB,email,password,StartDate,Job_Title):
    dbinit()
    person = Person(TD.first_name(),TD.last_name(),TD.domain_name(),TD.date_of_birth(minimum_age=17, maximum_age=85))
    conn = sqlite3.connect("TestData.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (First_Name,Last_Name,Birthdate,Email,Password,job_Title,StartDate) Values (?,?,?,?,?,?,?)",
    (person.first_name,person.last_name,person.DOB(),person.email(),create_password(16),Job_Title,StartDate))
    conn.commit()
    conn.close()

#user = Person(TD.first_name(),TD.last_name(),TD.domain_name(),TD.date_of_birth(minimum_age=17, maximum_age=85))

#print (user.first_name,user.last_name,user.email(),user.DOB())

create_users(Person(TD.first_name(),TD.last_name(),TD.domain_name(),TD.date_of_birth(minimum_age=17, maximum_age=85)),TD.job(),TD.date_this_century())

#def multi_create_users():
 #   i = 0 
 #   count = input("How many names would you like to generate?: ")
 #   while i < int(count):
 #       create_users()
 #       i += 1

#def create_customers():
#    connection = sqlite3.connect('TestData.db')
#    cursor = connection.cursor()
#    cursor.execute('CREATE TABLE IF NOT EXISTS CUSTOMERS ("CID" INTEGER,"Name" TEXT, "Birthdate" TEXT, "Address" TEXT, "Email" TEXT);')
#    cursor.execute('INSERT INTO CUSTOMERS VALUES(:CID, :Name, :Birthdate, :Address, :Email)',{'CID':TD.random_int(1,100), 'Name': TD.name(), 'Birthdate': str(TD.date_of_birth(minimum_age=17, maximum_age=85))
#    ,'Address': TD.address(), 'Email': TD.email()})
#    select_customers()
#    connection.commit()
#    connection.close()

#def multi_create_customers():
#    i = 0 
#    count = input("How many names would you like to generate?: ")
#    while i < int(count):
#        create_customers()
#        i += 1

#def create_part():
#    connection = sqlite3.connect('TestData.db')
#    cursor = connection.cursor()
#    partName = (TD.word()+'-'+str(TD.random_int(1,10000)))
#    cursor.execute('CREATE TABLE IF NOT EXISTS PARTS ("PID" TEXT, "Part_Name" TEXT, "Cost" real,"BaseCurrency" TEXT, "QTY" INTEGER);')
#    cursor.execute('INSERT INTO PARTS VALUES(:PID, :Part_Name, :Cost, :BaseCurrency, :QTY)',{'PID':TD.random_int(1,100), 'Part_Name': partName,'BaseCurrency':'£', 'Cost':TD.random_int(1,100)
#    ,'QTY': TD.random_int(1,100)})
#    connection.commit()
#    connection.close()

#def multi_create_parts():
#    i = 0 
#    count = input("How many parts would you like to generate?: ")
#    while i < int(count):
#        create_part()
#        i += 1
        

#def select_users():
#    connection = sqlite3.connect('TestData.db')
#    cursor = connection.cursor()
#    print ("############################")
#    print ("########### Users ##########")
#    print ("############################")
#    print("Name, Dob, Password, Email, job title, start date")
#    cursor.execute('SELECT * FROM Users')
#    for i in cursor.execute('SELECT UID,First_Name, Last_Name, Birthdate, Password, Email, Job_Title, StartDate FROM Users'):
#        print(i)
#    connection.close()
#    print ("############################")#

#def select_customers():
#    connection = sqlite3.connect('TestData.db')
#    cursor = connection.cursor()
#    print ("############################")
#    print ("######## Customers #########")
#    print ("############################")
#    cursor.execute('SELECT * FROM CUSTOMERS')
#    for i in cursor.execute('SELECT CID, Name, Birthdate, Address, Email FROM CUSTOMERS'):
#        print(i)
#    connection.close()
#    print ("#########################")

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
#    print ("#########################")

#def select_all_data():
#    select_customers()
#    print("\n")
#    select_users()
#    print("\n")
#    select_parts()
#    print("\n")

#def main():
#    init()

 
 #   opt1 = input("Do you want to READ or WRITE (R/W/eXit): ")
 #   if opt1.upper() == 'R':
 #       opt1a = input("What data would you like to read ? Customers ,Users ,Parts, All (C,U,P,A): ")
 #       if opt1a.upper() == 'C':
 #           select_customers()
 #       elif opt1a.upper() == 'U':
 #           select_users()
 #       elif opt1a.upper() == 'P':
 #           select_parts()
 #       elif opt1a.upper() == 'A':
 #           select_all_data()
 #       else:
 #           print ("Invalid selection")
 #   elif opt1.upper() == 'W':
 #           opt2 = input("What data would you like to Create ? Customers ,Users, Parts (C,U,P): ")
 #           if opt2.upper() == 'C':
 #                   opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
 #                   if opt2a.upper() == 'Y':
  #                      multi_create_customers()
  #                  elif opt2a.upper() == 'N':
  #                      create_customers()
  #                  elif opt2a.upper() == 'X':
  #                      print("Goodbye")
  #                      exit()

#            elif opt2.upper() == 'U':
#                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
#                    if opt2a.upper() == 'Y':
#                        multi_create_users()
#                    elif opt2a.upper() == 'N':
#                        create_users(firstName,lastName,str(TD.date_of_birth(minimum_age=17, maximum_age=85)),create_password(16),email,TD.job(),StartDate)
#                    elif opt2a.upper() == 'X':
#                        print("Goodbye")
#                        exit()
#            elif opt2.upper() == 'P':
#                    opt2a = input("Do you want to create more than one record? (Y/N/eXit): ")
#                    if opt2a.upper() == 'Y':
#                        multi_create_parts()
#                    elif opt2a.upper() == 'N':
#                        create_part()
#                    elif opt2a.upper() == 'X':
#                        print("Goodbye")
#                        exit()
 #           else:
  #              print ("Invalid selection")
#
 #   elif opt1.upper() == 'X':
  #      print("Goodbye")
   #     exit()
   # else:
   #     print("Invalid option please try again")
   
    #main()

#if __name__ == "__main__":
#    main()
    
