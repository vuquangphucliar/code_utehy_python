def tienthuephong(ngaythue,loaiphong):
    tienphong=0
    if loaiphong=="A":
        tienphong=ngaythue*200000
    elif loaiphong=="B":
        tienphong = ngaythue * 150000
    elif loaiphong=="C":
        tienphong = ngaythue * 130000
    else:
        tienphong=0
    return tienphong
print(tienthuephong(4,"B"))