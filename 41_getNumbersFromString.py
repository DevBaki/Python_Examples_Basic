import re
print("Enter strings")
inputString = input().split(' ')

lists = []
for i in inputString:
    if i.isdigit():
        lists.append(i)
print(lists)
