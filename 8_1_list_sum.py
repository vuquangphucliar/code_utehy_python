s=0
l=[]
n=int(input('Enter the number of elements, n= '))
for i in range(0,n,1):
    print('l[',i,']= ')
    x=float(input())
    l.append(x)
for i in l:  #for i in range(0,len(l),1):
    print(i)
    s+=i
print('The sum of list l is: ',s)
