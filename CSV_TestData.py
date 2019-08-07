#! /usr/bin/python3
import csv
import sqlite3
import random
from faker import Faker
TD = Faker('en_GB')

count =int(input('How many IDs should be generated? : '))

def create_test_data(amount):
    data = []
    for _ in range(0,amount):
        data.append(TD.name())
        data.append(TD.address())
    return data

with open ('TestData.csv', mode='w', newline='') as csvfile:
    fieldnames = ['name', 'address']
    csv_test_data = csv.writer(csvfile, delimiter=',', quotechar='"')
    for i in create_test_data(count):
        csv_test_data.writerow([i],)
