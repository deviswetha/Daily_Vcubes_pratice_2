''' 
4.Input = 5 
            1
           12
          123
         1234
        12345
'''

row = int(input('Enter the rows: '))
i = 1

while i <= row:
    j = 1
    print(' ' * (row - i), end='')  
    while j <= i:
        print(j, end='')  
        j += 1
    print()
    i += 1
