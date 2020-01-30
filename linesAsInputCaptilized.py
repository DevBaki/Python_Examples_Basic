print("Enter lines of sentences")
my_list=[]
while True:
    s=input()
    if s:
        my_list.append(s.upper())
    else:
        break

print(my_list)
