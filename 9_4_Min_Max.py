def findMax(*a):
    max=a[0]
    for i in a:
        if max<i:
            max=i
    return max
print(findMax(3,2))
print(findMax(3,2,6,7))
print(findMax(3,2,8,10,16,39,1))
