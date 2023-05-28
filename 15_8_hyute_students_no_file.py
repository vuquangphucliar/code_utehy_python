import pandas as pd

def nhap():
    SV=[]
    print('Nhập thông tin sinh viên ')
    while(True):
        MaSV = input('Mã sinh viên: ')
        hoten = input('Họ và tên sinh viên: ')
        lop = input('Lớp sinh viên: ')
        que = input('Quê quán: ')
        SV.append([MaSV,hoten,lop,que])
        return SV
def hien_thi(SLTK):
    print('Số liệu thống kê số lượng sinh viên nhập học năm 2019')

choose=0
while choose!=3:
    print('1. Nhập liệu')
    print('2. Hiển thị dữ liệu')
    print('3. Kết thúc')
    choose=int(input('Chọn một công việc: '))
    if choose==1:
        SLTK=nhap()
        print(SLTK)
    elif choose==2:
        hien_thi(SLTK)
    else:
        break