n = int(input())
arr = map(int, input().split())

list1 = list(arr)
second_highest = sorted(set(list1))[-2]
print(second_highest)
