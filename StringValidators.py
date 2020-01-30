inputString = input()

print(any(c.isalnum() for c in inputString))
print(any(c.isalpha() for c in inputString))
print(any(c.isdigit() for c in inputString))
print(any(c.islower() for c in inputString))
print(any(c.isupper() for c in inputString))


