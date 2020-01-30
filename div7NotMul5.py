def _div7AndNotMul ( n1, n2 ):
    l=[]
    for i in range(2000,3200):
        if (i%7==0) and (i%5!=0):
            l.append(str(i))
    return l


print(_div7AndNotMul(2000, 3201))