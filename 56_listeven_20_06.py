num = list(map(int, input("Enter numbers: ").split()))
l = []

for i in num:
    if i % 2 == 0:
        l.append(i)

print("Even numbers:", l)
