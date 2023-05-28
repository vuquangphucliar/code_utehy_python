def DNTT(c1,c2):
    return c2-c1
def tiendien(sodien):
    td=0
    if sodien<100:
        td=sodien*1500
    elif (sodien>=100) and (sodien<150):
        td=100*1500+(sodien-100)*2000
    else:
        td = 100 * 1500 +50*2000+ (sodien - 100) * 2500
    return td
QLTD=[]
while True:
    n=int(input('Nhap so luong khach hang: '))
    if n>0:
        break
for i in range(n):
    while True:
        makh=input('Ma KH: ')
        if makh!='':
            break
    while True:
        tenkh=input('Ten KH: ')
        if tenkh!='':
            break
    while True:
        cs1=int(input('Chi so thang truoc: '))
        if cs1>=0:
            break
    while True:
        cs2=int(input('Chi so thang nay: '))
        if (cs2>=cs1) and (cs2<99999):
            break
    QLTD.append([makh,tenkh,str(cs1),str(cs2),str(DNTT(cs1,cs2)),str(tiendien(DNTT(cs1,cs2)))])

print('\t'.join(['Ma KH', 'Ten KH', 'Chi so 1', 'Chi so 2', 'Dien nang', 'Tong tien'])+'\n')
for khachhang in QLTD:
    print('\t'.join(khachhang)+'\n')

print('Danh sach khach hang co tien dien tieu thu trong thang >300')
print('\t'.join(['Ma KH', 'Ten KH', 'Chi so 1', 'Chi so 2', 'Dien nang', 'Tong tien'])+'\n')
k=1
for khachhang in QLTD:
    if int(khachhang[4])>300:
        print('\t'.join(khachhang) + '\n')
        k+=1

f=open('td.txt','w',encoding='utf-8')
for khachhang in QLTD:
    f.write('\t'.join(khachhang)+'\n')
f.close()