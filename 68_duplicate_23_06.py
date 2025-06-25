'''
Write a  Python program to print and find the duplicate values in the list of values 
Input: [1,2,3,4,5,1,6]
Output : [1]

'''
l=[1,2,3,4,5,1,6]

duplicates = []

for i in l:
    if l.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate values:", duplicates)
