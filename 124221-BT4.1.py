l = []
tong = 0
n = int(input("Moi nhap so phan tu trong mang :"))
c = 0
for i in range(n):
    x = int(input("Nhap phan tu: "))
    l.append(x)
for i in l:
    if i % 2 == 0:
        tong = tong + i
print(tong)
l.sort()
l.reverse()
print(l)
k = int(input("Moi nhap gia tri can tim :"))
for i in range(n):
    if k == l[i]:
        print("Phan tu can tim nam o vi tri", i)
        c=c+1
if c == 0:
    print("Khong ton tai ")
for i in range(len(l)):
    if l[i] < 0:
        l.remove(l[i])
print(l)

