lists = []
tuples = ()
while True:
    inputStrings = input()
    if not inputStrings:
        break

    lists.append(tuple(inputStrings.split(",")))

print(sorted(lists, key=lambda x: x[0]))
