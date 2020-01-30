strings = []
while True:
    inputString = input()
    if inputString:
        strings.append(inputString)
    else:
        break

sets = sorted(list(set(strings)))

for li in sets:
    print(li)
