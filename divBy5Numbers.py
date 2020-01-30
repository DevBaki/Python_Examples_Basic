strings = []
items = [x for x in input().split(',')]
for li in items:
    if int(li) % 5 == 0:
        strings.append(li)

print("Numbers which are divisible by 5: ")
for i in strings:
    print(i)
