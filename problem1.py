##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
count = 0
User = ""
Pass = ""
while User != "admin" and Pass != "12345":
    User = (input("Please enter username "))
    Pass = (input("Please enter password "))
    count = count + 1
    if User == "admin" and Pass == "12345":
        print ("Access granted")
    else:
        print ("Access denied")
    if count > 2:
        break