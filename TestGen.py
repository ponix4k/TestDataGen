
#! /usr/bin/python
from faker import Faker
fake_data = Faker('en_GB')#this can be set to other languages see docs for more info
##########################
#create a fake name
##########################
#name = fake_data.name();print(name)
##########################
#create a fake address
##########################
#address = fake_data.address();print(address)
##########################
#create a fake email
##########################
#email = fake_data.safe_email();print(email)

##########################
#create a simple fake profile
##########################
#profile = fake_data.simple_profile()
#for k,v in profile.items():
#   print('{} :{}'.format(k,v))
#display name,address,email
#print('Name:  {},Address:  {}, Email: {}'.format(name,addres,email))
##########################
# generate a lagre set of data
##########################
#for _ in range(0,10):
#    print(fake_data.name())
#Count = int
#Count = input('How many should i generate? : ')

#def create_names_list(how_many):
#    names = []
#   for _ in range(0,how_many):
#      names.append(fake_data.name())
#  return names
#  print (names)
##########################
#create_names_list(5)
##########################
class Customers:
    def __init__(self, name, address, email):
       self.name = name
       self.address = address
       self.email = email

 #   def __repr_(self):
 #       return 'name: {}, address: {}, email: {}'.format(self.name,self.address,self.email)

#Cust1 = Customers(fake_data.name(),fake_data.address(),fake_data.email())
#print (Cust1)
customers_list = []
for i in range (10):
    customers_list.append(Customers(fake_data.name(),fake_data.address(),fake_data.safe_email()))
for i in customers_list:
    print(1,'/n')
