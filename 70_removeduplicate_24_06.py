'''
2.Write a Python program to remove duplicate elements from a given list.?
Input: [1, 2, 2, 3, 4, 4, 5]
Output:[1, 2, 3, 4, 5]
'''
l = [1, 2, 2, 3, 4, 4, 5]

for i in l:
    while l.count(i) > 1:
        l.remove(i)

print("Output:", l)
