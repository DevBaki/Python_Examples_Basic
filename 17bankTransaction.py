balance = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operator = values[0]
    amount = int(values[1])
    if operator == "D":
        balance = balance + amount
    elif operator == "W":
        if balance >= amount:
            balance = balance - amount
        else:
            print("You cant withdraw , your balance is less than balance")
            pass
    elif not s:
        break
    else:
        pass

print("you have remaining balance is : ", balance)
