print("Please a string:")
inputString = input()
dict1 = {"UPPER": 0, "LOWER": 0}

for i in inputString:
    if i.isalpha():
        if i.islower():
            dict1["LOWER"] += 1
        elif i.isupper():
            dict1["UPPER"] += 1
        else:
            pass

print("Lower case letters:", dict1["LOWER"])

print("Upper case letters:", dict1["UPPER"])
