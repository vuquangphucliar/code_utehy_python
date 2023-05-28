x=int(input('Nhập vào giá trị của x: '))
while x<10:
    x = int(input('Mời bạn nhập lại giá trị của x: (x>10)'))
n=int(input('Nhập vào giá trị của n: '))
while (n<0) or (n>20):
    n = int(input('Mời bạn nhập lại giá trị của n: (0<n<20)'))
s=0
for i in range(1,n+1):
    s=s+x/i
#i=1
#while i<=n:
#    s=s+x/i
#    i+=1
print('Tổng S= ',s)