print("Enter a number")
number = input()

sumOfStatement = 0.0
for i in range(1, (int(number) + 1)):
    sumOfStatement = sumOfStatement + float(i / (i + 1))

print(sumOfStatement)
