#Write a Python program to check give number is prefect cube or not without using loops

import math

num = int(input("Enter a number: "))
i = round(num ** (1/3))

if i ** 3 == num:
    print("It is a perfect cube")
else:
    print("It is not a perfect cube")
