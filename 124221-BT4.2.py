SV=[]
n=int(input("Nhap so sinh vien: "))
for i in range(n):
    tam=[]
    masv=input("Ma SV: ")
    tam.append(masv)
    ten=input("Ten SV: ")
    tam.append(ten)
    ns=int(input("Nam sinh: "))
    tam.append(ns)
    dtb=float(input("Diem TB: "))
    tam.append(dtb)
    SV.append(tam)
SV[1][3]=4.0
for sv in SV:
    print(f'{sv[0]:8} {sv[1]:20} {sv[2]:5} {sv[3]:5.2}')
