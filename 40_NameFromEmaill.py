print("Print Email Address")
emailAddress = input()

print("The name in the email is : ", emailAddress.split('@')[0])
print("The name in the domain  is : ", (emailAddress.split('@')[1]).split('.')[0])
