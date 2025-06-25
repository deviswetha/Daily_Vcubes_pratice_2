# Write a program to find the largest among three numbers using nested if statements

n1=int(input('enter a number'))
n2=int(input('enter a number'))
n3=int(input('enter a number'))

if n1>n2 and n1>n3:
    print('biggest number',n1)
    
    if n2>n1 and n2>n3:
        print('biggest number',n2)
else:
    print('biggest number',n3)