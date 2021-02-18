#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
User = ""
Pass = ""
while User != "admin" and Pass != "12345":
    User = (input("Please enter username "))
    Pass = (input("Please enter password "))

    if User == "admin" and Pass == "12345":
        print ("Access denied")
    else:
        print ("Access granted")
    