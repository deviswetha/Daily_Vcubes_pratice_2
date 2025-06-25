#Find the least common multiple (LCM) and greatest common divisor (GCD) of two numbers

n1=int(input('enter n1:'))
n2=int(input('enter n2:'))

if n1>n2:
    small=n1
else:
    small=n2

d=2

while d<=small:
    if n1%d==0 and n2%d==0:
        print('lcd is:',d)
        break
    d+=1
else:
    print('no lcd')
