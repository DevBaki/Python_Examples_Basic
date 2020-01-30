concatString: str = ""
while True:
    string1 = input()

    if string1:
        concatString = concatString + string1
    else:
        break

print("Concat string is: ", concatString)
