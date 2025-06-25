#Write a Python program that checks if a given year is a century year (ending in '00')


y=int(input('enter the year:'))

if y % 100==0:
    print(' ends with 00')
else:
    print (' not ends with 00')
