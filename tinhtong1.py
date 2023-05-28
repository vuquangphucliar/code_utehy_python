#Nhập n từ bàn phím. n>0
while True:
    n=int(input("Nhập giá trị của n: "))
    if n>0:
        break
    else:
        print("Bạn phải nhập n>0 ")
s=0
for i in range(1,n+1,1):
    s=s+(2*i-1)/(2*i) #s=s+1/i
print("Tổng S = 1+ 1/2+...1/",n," = ",s)
