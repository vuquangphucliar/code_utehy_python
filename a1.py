def danh_sach_cong_nhan():
    dscn = {}
    while True:
        macongnhan = str(input('Mã công nhân (Khoảng trắng để dừng nhập): ')).upper()
        if macongnhan == ' ':
            break
        elif macongnhan == '':
            print('Mã khác xâu rỗng!')
            continue
        else:
            while True:
                tencongnhan = str(input('Tên công nhân : ')).title()
                if tencongnhan != '':
                    break
            while True:
                namsinh = input('Năm sinh : ')
                if namsinh.isdigit() == True:
                    namsinh = int(namsinh)
                    if 1960 < namsinh < 2001:
                        break
            while True:
                congnhat = input('Số ngày công : ')
                if congnhat.isdigit() == True:
                    congnhat = int(congnhat)
                    if 0 < congnhat <= 31:
                        break
        dscn.update({macongnhan:[tencongnhan, namsinh, congnhat]})
    return dscn
# ten - namsinh - cong nhật
def tinh_tuoi(namsinh):
    return 2022 - namsinh
def luong_ghi_chu(ngaylamtrongthang):
    if 0 < ngaylamtrongthang < 15:
        ghichu = 'Nghỉ nhiều'
        luong = 15000 * ngaylamtrongthang
    elif 31 >= ngaylamtrongthang >= 25:
        ghichu = 'Chăm chỉ'
        luong = 20000 * ngaylamtrongthang
    else:
        ghichu = ''
        luong = 18000 * ngaylamtrongthang
    return [luong, ghichu]
dscn = danh_sach_cong_nhan()
for cn in dscn:
    tuoi = tinh_tuoi(dscn[cn][1])
    dscn[cn].append(tuoi)
    l_vs_gc = luong_ghi_chu(dscn[cn][2])
    dscn[cn].append(l_vs_gc[0])
    dscn[cn].append(l_vs_gc[1])
# ten - nam sinh - cong nhat - tuoi - luong - ghi chu
print('Mã CN | Tên công nhân | Tuổi | SN làm việc | Lương | Ghi chú')
for cn in dscn:
    print(f'{cn} \t {dscn[cn][0]} \t {dscn[cn][3]} \t {dscn[cn][2]} \t {dscn[cn][4]} \t {dscn[cn][5]}')
k = open('CongNhan(bài 6.17).csv', 'w', encoding='utf-16')
k.write('Mã CN | Tên công nhân | Tuổi | SN làm việc | Lương | Ghi chú\n')
for cn in dscn:
    k.write(f'{cn} \t {dscn[cn][0]} \t {dscn[cn][3]} \t {dscn[cn][2]} \t {dscn[cn][4]} \t {dscn[cn][5]} \n')
k.close()