def nhap():
    SV=[]
    print('Nhập thông tin sinh viên ')
    while(True):
        MaSV = input('Mã sinh viên: ')
        if MaSV=='':
            break
        hoten = input('Họ và tên sinh viên: ')
        lop = input('Lớp sinh viên: ')
        que = input('Quê quán: ')
        SV.append([MaSV,hoten,lop,que])
    return SV
def hien_thi(SV):
    masv=[]
    hoten=[]
    lop=[]
    que=[]
    for sinhvien in SV:
        masv.append(sinhvien[0])
        hoten.append(sinhvien[1])
        lop.append(sinhvien[2])
        que.append(sinhvien[3])
choose=0
while choose!=3:
    print('1. Nhập liệu')
    print('2. Hiển thị dữ liệu')
    print('3. Kết thúc')
    choose=int(input('Chọn một công việc: '))
    if choose==1:
        SV=nhap()
        print(SV)
    elif choose==2:
        hien_thi(SV)
        for i in range(0,len(SV),1):
            print(SV[i])
    else:
        print('Bạn hãy chọn 1, 2 hoặc 3')