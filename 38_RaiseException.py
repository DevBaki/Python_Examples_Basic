print("Please enter number")
inputString = input()
'''If you enter something then no exception'''
if inputString:
    print("you have entered :", inputString)
else:
    raise Exception("you didn't entered anything")
