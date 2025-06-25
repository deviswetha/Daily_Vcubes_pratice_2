# Write a Python program to check if the given number is an Armstrong number or not

num = int(input("Enter a number: "))
digits = len(str(num))
s = sum(int(digit) ** digits for digit in str(num))

if s == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
