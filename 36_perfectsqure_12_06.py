# Write a python program to check give number is prefect square or not without using loops
import math

num=int(input('enter the number:'))

i= math.isqrt(num)

if i*i==num:
    print('it is a perferct square')
   
else:
    print('it is not a perfect square')
