lists = []
for i in range(1, 21):
    lists.append(i)

'''print all the elements in the list'''
print("Elements in List:", [x ** 2 for x in lists])

'''print First 5 elements in the list'''
print("First 5 elements in list", [x ** 2 for x in lists[:5]])

'''print First 5 elements in the list'''
print("Last 5 elements in list", [x ** 2 for x in lists[-5:]])

'''print all elements except First 5 elements in the list'''
print("Last 5 elements in list", [x ** 2 for x in lists[5:]])
