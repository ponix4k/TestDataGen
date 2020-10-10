import secrets
import string
import sqlite3

from faker import Faker

TD = Faker('en_GB')#this can be set to other languages see docs for more info

def dbinit():
    conn = sqlite3.connect("TestData.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS USERS (UID INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Birthdate TEXT DEFAULT '01-01-1899',Contact_Number TEXT,Email TEXT, Password TEXT, Job_Title TEXT DEFAULT 'Worker',StartDate TEXT DEFAULT '01-01-1899');")
    conn.commit()
    conn.close()
    print("Database Initalised")

def create_password(stringLength):
    chars = string.ascii_letters + string.digits + string.punctuation
    password =''.join(secrets.choice(chars) for i in range(stringLength))
    return password

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

def main():
    dbinit()

if __name__ == "__main__":
    main()