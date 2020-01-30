while True:
    stringInput1 = input()
    stringInput2 = input()
    if stringInput1 and stringInput2:
        if len(stringInput1) > len(stringInput2):
            print(stringInput1 + "has max length")
        else:
            print(stringInput2 + "has max length")
    else:
        break
