def Avg(items):
    sum_numbers=0
    for i in items:
        sum_numbers=sum_numbers+i
    return sum_numbers/len(items)
a=[33,344,323]
print(Avg(a))
#print(Avg(3,4))
