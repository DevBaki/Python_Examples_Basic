def addFunc(a, b):
    return a + b


print("Please enter number1 and number2")
numbers = input().split(",")
print(addFunc(int(numbers[0]), int(numbers[1])))
