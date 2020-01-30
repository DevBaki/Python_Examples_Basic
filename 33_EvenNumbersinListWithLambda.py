li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNumbers = filter(lambda x: x % 2 == 0, li)
print([x for x in evenNumbers])

squaredNumbers = map(lambda x: x ** 2, li)
print([x for x in squaredNumbers])

evenNumbers = filter(lambda x: x % 2 == 0, range(1, 21))
print([x for x in evenNumbers])

evenNumbers1 = map(lambda x: x % 2 == 0, range(1, 21))
print([x for x in evenNumbers1])
