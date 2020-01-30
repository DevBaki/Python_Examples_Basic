fibLists = []


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n - 1) + f(n - 2)


f(5)
print([f(x) for x in range(0, 5)])
