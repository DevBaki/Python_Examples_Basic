import math
c=50
h=30
values=[]
try:
    my_list=[]
    while True:
        my_list.append(int(input()))
except:
    print(my_list)

for d in my_list:
    values.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(values)


