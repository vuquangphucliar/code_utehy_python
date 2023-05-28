#Câu 2:
def tiendien(sokw):
    if sokw<=100:
        td=sokw*1400
    elif 101<=sokw<150:
        td=100*1400+(sokw-100)*1750
    elif  151<=sokw<=250:
        td=100*1400+50*1750+(sokw-250)*2000
    else:
        td=100*1400+50*1750+100*2000+(sokw-250)*2500
    return int(td*1.1)
#Câu 1
chungcu=[]
n=int(input("Nhap so phong chung cu "))
for i in range(n):
    while True:
        phong=input("Nhap so hieu phong: ")
        if phong!="":
            break
    while True:
        toanha=input("Nhap so hieu toa nha: ")
        if toanha!="":
            break
    while True:
        chuho=input("Nhap ten chu ho: ")
        if chuho!="":
            break
    while True:
        kw=int(input("Nhap so dien tieu thu: "))
        if kw>0:
            break
    chungcu.append([phong,toanha,chuho,kw,tiendien(kw)])
#Câu 3
print('\t'.join(["So hieu phong","Toa nha","        Chu ho     ","    so dien   ","Tien dien phai tra"]))
for cc in chungcu:
    print(f'{cc[0]:15} {cc[1]:10} {cc[2]:20} {cc[3]:5} {cc[4]:10}')
#Câu 4
fcc=open("phuchung.txt","w",encoding="utf-8")
fcc.write('\t'.join(["So hieu phong","Toa nha","        Chu ho     ","   so dien   ","Tien dien phai tra"])+'\n')
for cc in chungcu:
    fcc.write(f'{cc[0]:15} {cc[1]:10} {cc[2]:20} {cc[3]:5} {cc[4]:10} \n')