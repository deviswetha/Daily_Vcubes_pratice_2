#Write a Python program to check give number is prefect cube or not


num = int(input("Enter a number: "))
i = 0

while i * i * i <= num:
    if i * i * i == num:
        print("It is a perfect cube")
        break
    i += 1
else:
    print("It is not a perfect cube")
