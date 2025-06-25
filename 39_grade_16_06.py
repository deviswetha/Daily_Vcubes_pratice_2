#1.Determine the grade from a given score.
##Input: score = 85
#Output: Grade: B


num=int(input('Enter the score:'))

if num>85:
    print('grade A')
elif num<=65:
    print('grade C')
else:
    print('grade B')
