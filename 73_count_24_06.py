'''
4.Write a Python program to count how many times a specific element occurs in a given list.
Input: List: [1, 2, 2, 3, 4, 2, 5]
            Element to count: 2
Output: 2 appears 3 times
'''
num = list(map(int, input("Enter a list of numbers: ").split()))
element =int(input("Enter the element:")) 

count = num.count(element)

print(f"appear {count} times")
