#! /usr/bin/python3

Server = (input('Enter Servername to use: '))
Port =(input('Enter port (default is 3306): '))
Database =(input('Enter database name to use: '))
User = (input('Enter Username you wish to login with: '))
Password = (input('Enter Password to use for login: '))

f= open("Connection.conf","w+")
print ('Configuration Saved')
print('[connector_python]')
print('host=',Server)
print('Port=',Port)
print('database=',Database)
print('user=',User)

f.write("[connector_python]\n")
f.write("host="+Server+"\n")
f.write("port="+Port+"\n")
f.write("database="+Database+"\n")
f.write("user="+User+"\n")
f.write("password="+Password+"\n")
