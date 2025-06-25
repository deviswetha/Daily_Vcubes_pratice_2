'''
Write a Python program to print whether the given number is a strong number or not 
Input: 145
Output: strong number
'''


import math

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += math.factorial(digit)
    temp = temp // 10

if sum == num:
    print("Strong number")
else:
    print("Not a strong number")
