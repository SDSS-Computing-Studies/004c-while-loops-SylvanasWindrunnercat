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
c = "admin"
a = ""
g = 0

while a != c:
    a = input("The username is:").strip()
    if a != c:
        print("Access denied")
    g = g + 1
    if g == 3:
        exit()

d = "12345"
b = ""
t = 0

while b != d:
    b = input("The password is:").strip()
    if b != d:
        print("Access denied")
    t = t + 1
    if t == 3:
        exit()
print("Access granted")