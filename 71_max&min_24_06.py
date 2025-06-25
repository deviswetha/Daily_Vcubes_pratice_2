'''
1.Write a Python program to find the maximum and minimum values in a given list of integers.?
Input: [2, 10, 3, 6, 1]
Output: Max: 10  
        Min: 1
'''

num = list(map(int, input("Enter numbers: ").split()))
l = []

max_v=float('-inf')
min_v=float('+inf')

for i in num:
    if i>max_v:
        max_v=i
    if i<min_v:
        min_v=i
print(min_v)
print(max_v)