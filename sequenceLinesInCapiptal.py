strings = []
while True:
    inputString = input()
    if inputString:
        strings.append(inputString.upper())
    else:
        break


for li in strings:
    print(li)