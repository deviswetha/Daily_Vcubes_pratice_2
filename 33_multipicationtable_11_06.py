# Generate a multiplication table for a given number using a while loop

n=int(input('enter the number:'))

i=1

while i<=10:
    print(n,'*',i,'=',i*n)
    i=i+1

