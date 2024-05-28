import random
print("welcome to random password generator!")
randomchars="abcdefghijklmnpqrstuvwxyz1234567890!@#$%^&*()_+"
numberofpwds=int(input("plese enter the number of password:"))
pwdlength=int(input("plese enter the length of password:"))

print("your random password:")
for i in range(numberofpwds):
    pwd=""
    for chars in range(pwdlength):
        pwd=pwd+random.choice(randomchars)
    print(pwd)
               
