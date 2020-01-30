import re

print("Please Enter Password: ")
password = input()
if re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])", password) and (6 <= len(password) <= 12):
    print("password is validated")
else:
    print("password is invalid")
