dict1 = {}
for i in range(1, 5):
    dict1[i] = int(i) ** 2

print(dict1)
print("Keys are : ", [x for (x, v) in dict1.items()])
print("Values are ", [v for (x, v) in dict1.items()])
