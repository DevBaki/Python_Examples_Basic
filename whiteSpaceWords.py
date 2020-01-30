print("Enter strings")
while True:
    s = input()
    if s and s!='break':
        [].append(s)
    else:
        break
print(isinstance(2, int))
print([])
print(sorted(set([])))


s = input()
words = [word for word in s.split(" ")]
print(sorted(list(set(words))))


