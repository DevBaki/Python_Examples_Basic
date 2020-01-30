from operator import itemgetter

if __name__ == '__main__':
    lists = []
    p = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l = [name, score]
        lists.append(l)

# min of all elements
mn = min(lists, key=itemgetter(1))[1]
# remove elements equal to min
filtered = [x for x in lists if x[1] != mn]
# get min of remaining
mn_fil = min(filtered,key=itemgetter(1))[1]
# filter remaining
out = [x for x in filtered if x[1] == mn_fil]
secondlowests=sorted([item[0] for item in out])
for i in secondlowests:
    print(i)