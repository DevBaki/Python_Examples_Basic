def swap_case(s):
    list1 = []
    for i in s:
        if i.isupper():
            list1.append(i.lower())
        elif i.islower():
            list1.append(i.upper())
        else:
            list1.append(i)
    return ''.join(list1)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
