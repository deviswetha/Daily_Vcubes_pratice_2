# Write a Python program that classifies a person's age: child, teenager, adult, and senior

n=int(input("enter the age:"))

if n<=12 :
    print('child')
elif n<=19:
    print('teenage')
elif n<=59:
    print('adult')
else:
    print('senior')