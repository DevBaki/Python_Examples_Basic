def EvenYield(num):
    ii = 0
    while ii <= num:
        if ii % 2 == 0:
            yield ii
        ii + 1


n = int(input())
values = []
for i in EvenYield(n):
    values.append(str(i))

print(",".join(values))
