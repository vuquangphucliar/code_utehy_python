import pandas as pd
import matplotlib.pyplot as plt
def nhap():
    txt_file = open('utehy.txt', 'w', encoding='utf-8')
    DSKhoa=['CNTT','NNgu','KTe','M&TT','Đ-ĐT','CKĐL','CKCT']
    SLTK=[]
    tt=0
    for KHOA in DSKhoa:
        tt+=1
        print('Nhập số liệu sinh viên nhập học của khoa ',KHOA)
        while(True):
            sl_trung_tuyen = int(input('Số lượng trúng tuyển: '))
            if (sl_trung_tuyen >= 0):
                break
        while(True):
            sl_nhap_hoc=int(input('Số lượng nhập học: '))
            if (sl_nhap_hoc>=0) and (sl_nhap_hoc<=sl_trung_tuyen):
                break
        tyle=round(sl_nhap_hoc/sl_trung_tuyen*100)
        SLTK.append([KHOA,sl_trung_tuyen,sl_nhap_hoc,tyle])
        txt_file.write('\t'.join([str(tt),str(sl_nhap_hoc), str(sl_trung_tuyen),str(tyle)])+'\n')
    txt_file.close()
    return SLTK
def read_file():
    allData = []
    SLTK = []
    sl_nhap_hoc = []
    sl_trung_tuyen = []
    ty_le_nhap_hoc = []
    KHOA = ['CNTT', 'NNgu', 'KTe', 'M&TT', 'Đ-ĐT', 'CKĐL', 'CKCT']
    f_name=open("utehy.txt","r",encoding='utf-8')
    data = f_name.readlines()  # read the text file
    for line in data:
        allData = line.strip().split("\t")  # get a list containing all the numbers in the file
        sl_nhap_hoc.append(allData[1])
        sl_trung_tuyen.append(allData[2])
        ty_le_nhap_hoc.append(allData[3])
    for i in range(0, len(sl_nhap_hoc)):
        sl_nhap_hoc[i] = int(sl_nhap_hoc[i])
    for i in range(0, len(sl_trung_tuyen)):
        sl_trung_tuyen[i] = int(sl_trung_tuyen[i])
    for i in range(0, len(ty_le_nhap_hoc)):
        ty_le_nhap_hoc[i] = int(ty_le_nhap_hoc[i])
    SLTK.append([KHOA, sl_trung_tuyen, sl_nhap_hoc,ty_le_nhap_hoc])
    f_name.close()
    return  SLTK

def hien_thi(SLTK):
    print('Số liệu thống kê số lượng sinh viên nhập học năm 2022')
    print('\t'.join(['Khoa','| SL trúng tuyển','| SL nhập học','| Tỷ lệ SV nhập học']))
    print('\t'.join(['-------','| -----------------','| -------------','| -----------------']))
    for solieu in SLTK:
        sl_nhap_hoc=solieu[1]
        sl_trung_tuyen=solieu[2]
        ty_le_nhap_hoc=solieu[3]
    for i in range(0,len(DSKhoa)):
        print(DSKhoa[i],'\t|\t',end='')
        print(sl_nhap_hoc[i],'\t\t\t|\t',end='')
        print(sl_nhap_hoc[i],'\t\t|\t',end='')
        print(ty_le_nhap_hoc[i])
def veBieuDo(Khoa,SL_nhap_hoc,Y_label,ten_Bieudo):
    print(Khoa)
    print(SL_nhap_hoc)
    plt.xlabel('Khoa')
    plt.ylabel(Y_label)
    ind_Fact=range(len(Khoa))
    plt.bar(ind_Fact,SL_nhap_hoc,align='center')
    plt.xticks(ind_Fact,Khoa)
    plt.title(ten_Bieudo)
    for x,y in zip(ind_Fact,SL_nhap_hoc):
        plt.text(x+0.02,y+0.05,"%d"%y,ha='center',va='bottom')
    plt.show()

DSKhoa = ['CNTT','NNgu','KTe','M&TT','Đ-ĐT','CKĐL','CKCT']
sl_nhap_hoc = []
sl_trung_tuyen = []
ty_le_nhap_hoc = []
choose=0
while choose!=4:
    print('1. Nhập liệu')
    print('2. Hiển thị dữ liệu')
    print('3. Thống kê dữ liệu bằng biểu đồ')
    print('4. Kết thúc')
    choose=int(input('Chọn một công việc: '))
    if choose==1:
        SLTK=nhap()
        print(SLTK)
    elif choose==2:
        SLTK=read_file()
        hien_thi(SLTK)
    elif choose==3:
        SLTK = read_file()
        for solieu in SLTK:
            sl_nhap_hoc = solieu[2]
            sl_trung_tuyen = solieu[1]
            ty_le_nhap_hoc = solieu[3]

        veBieuDo(DSKhoa,sl_nhap_hoc,'Số lượng nhập học','Số lượng SV nhập học năm học 2019')
        veBieuDo(DSKhoa,ty_le_nhap_hoc,'Tỷ lệ ','Tỷ lệ SV nhập học năm học 2019')

        print(sl_trung_tuyen)
    else:
        print('Hãy nhấn phím 1,2,3 hoặc 4 để chọn chức năng')