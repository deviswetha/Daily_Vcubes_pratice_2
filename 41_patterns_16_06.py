'''
5.Pattern:
Input : 5
        A	
       AB
      ABC
     ABCD
    ABCDE
'''



row=int(input('Enter the rows:'))

i=1
space=' '
while i<=row:
    acii=65
    j=1
    print(' '*(row-i),end= '')
    while j<=i:
        print(chr(acii),end="")
        j=j+1
        acii=acii+1
    print()
    i=i+1
