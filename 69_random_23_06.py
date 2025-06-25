'''
Write a Python program to print 1 to 100 random even numbers
'''

import random
                 
number=random.randint(1,100)
 
s=0
if number%2==0:
    s=number+s
    print(number)
