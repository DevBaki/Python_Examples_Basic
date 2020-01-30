lists = []
for i in range(1, 21):
    lists.append(i)

'''Convert list to tuple'''
newTuple = tuple(lists)

'''print tuple'''
print(newTuple)
halfLength = len(newTuple) / 2

'''print first half of  tuple'''
print("first half of tuple:", newTuple[:int(halfLength)])

'''print last half of  tuple'''
print("last half of the tuple", newTuple[int(halfLength):])

'''Print even numbers in Tuple'''
print("Even numbers in tuple", [x for x in newTuple if x % 2 == 0])
