a=int(input('Nhập A : '))
b=int(input('Nhập b : '))
list_a=[];list_b=[];list_c=[]
for i in range(1,a+1):
    if a%i==0:
        list_a.append(i)
for j in range(1,1+b):
    if b%j==0:
        list_b.append(j)
list_a.sort;list_b.sort
list_a.reverse();list_b.reverse()
for k in list_a:
    for f in list_b:
        if k==f:
            list_c.append(k)
            break
print(f'Lowest common divisor {a} and {b} is {list_c[0]} ')
