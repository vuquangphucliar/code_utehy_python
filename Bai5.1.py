def func(*x):
    s=0
    for i in x:
        s=s+i
    return  s
print(func(2,3,4,6,8,9))