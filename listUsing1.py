# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# arr = []
# p=0
# for i in range(x+1):
#     for j in range(y+1):
#         if j+1!=n:
#             arr.append()


x, y, z, n = int(input()), int(input()), int(input()), int(input())
arr = []
p = 0

for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if i + j + k != n:
                    arr.append([])
                    arr[p] = [i, j, k]
                    p = p + 1

print(arr)

# print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])
