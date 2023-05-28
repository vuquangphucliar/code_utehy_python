#Bài tập 5.3. Xét hạnh kiểm sinh viên

hoten = input("Nhận vào họ và tên ")
while True:
    namsinh = int(input('năm sinh: '))
    if (namsinh>=1950) and (namsinh<=2005):
        break
diem = float(input('Nhập điểm trung bình: '))
if diem >= 9:
    xeploai="Xuất sắc"
elif (diem>=7.5)and (diem<9):
    xeploai = "Tốt"
elif (diem >= 6) and (diem < 7.5):
    xeploai = "Khá"
elif (diem >= 5.5) and (diem < 6):
    xeploai = "Trung bình"
elif (diem >= 4) and (diem < 5.5):
    xeploai = "Yếu"
else:
    xeploai="Kém"
print('Xếp loại hạnh kiểm của bạn ', hoten,', sinh năm ', namsinh, ", là: ", xeploai)
