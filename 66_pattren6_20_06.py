n=int(input('enter the number:'))

for i in range((2*n)-1):
    for j in range(n):
        if j<=i and i+j<=8:
          print("*",end=" ")
        else:
           print(" ",end=" ")

    print()