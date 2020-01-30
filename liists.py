if __name__ == '__main__':
    N = int(input())

lists = []
for i in range(N):
    letter = input().split(' ')
    if letter[0] == 'insert':
        lists.insert(int(letter[1]), int(letter[2]))

    if letter[0] == 'remove':
        lists.remove(int(letter[1]))

    if letter[0] == 'append':
        lists.append(int(letter[1]))

    if letter[0] == 'sort':
        lists.sort()

    if letter[0] == 'print':
        print(lists)

    if letter[0] == 'reverse':
        lists.reverse()

    if letter[0] == 'pop':
        lists.pop()


