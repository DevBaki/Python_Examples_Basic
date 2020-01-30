lists = []

print("Enter number1")
num1 = int(input())
print("Enter number2")
num2 = int(input())
for i in range(num1, num2):
    if int(i) % 2 == 0:
        lists.append(i)

print(','.join(map(str, lists)))
