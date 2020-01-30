inputString = input()
d = {"DIGITS": 0, "LETTERS": 0}

for i in inputString:
    if i.isdigit():
        d["DIGITS"] += 1
    elif i.isalpha():
        d["LETTERS"] += 1
    else:
        pass

print("DIGITS:", d["DIGITS"])
print("LETTERS:", d["LETTERS"])

