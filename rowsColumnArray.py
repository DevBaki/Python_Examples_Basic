print("Enter X:")
x=int(input())

print("Enter Y")
y=int(input())

multi_list = [[0 for col in range(y)] for row in range(x)]

print(multi_list)

for row in range(x):
    for col in range(y):
        multi_list[row][col]=row*col

print(multi_list)

