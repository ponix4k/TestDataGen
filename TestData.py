#! /usr/bin/python
import random
from faker import Faker
TD = Faker('en_GB')#this can be set to other languages see docs for more info
var1 = input("How Many Identities should be generated? : ")
count = (int(var1))
class Customers:
        def __init__(self, name, address, email):
            self.name = name
            self.age = random.randint(18,65)
            self.address = address
            self.email = email
        def __repr__(self):
            return 'Name: {}\nAge: {}\nAddress: {},\nEmail: {},'.format(self.name,self.age,self.address,self.email)

customer1 = Customers(TD.name(),TD.address(),TD.email())
for _ in range(0,count):
    print("##########  START  ##########")
    print(customer1)
    print("##########   END  ###########")
    print("")
