import random
char ="qwertyuiopasdfghjklmnbvcxz1234567890"
no_pass =input("enter no of passwords you need")
digit =input("enter no of digits :")
no_pass =int(no_pass)
digit = int(digit)
for p in range(no_pass):
    password = ''
    for c in range(digit):
        password += random.choice(char)
    print(password)
