'''
3.Write a Python program to find the sum of all odd numbers in a given list of   integers.?
Input: [1, 2, 3, 4, 5, 6, 7]
Output: Sum of odd numbers: 16
'''

num = list(map(int, input("Enter a list of numbers: ").split()))

s=0
for i in num:
    if i % 2 !=0:
        s+=i
print('sum of odd numbers:',s)