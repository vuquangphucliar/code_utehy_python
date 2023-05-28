def dtb(*a):
    tong=0
    dem=0
    for i in a:
        tong=tong+i
        dem=dem+1
    tb=round(tong/dem,1)
    return tb
def xl(*a):
    kq=""
    for i in a:
        if i<5:
            kq="Thi lai"
            break
        else:
            kq="Khong thi lai"
    return kq
print(dtb(5.70,3.50,6.40))
print(xl(5.70,3.50,6.40))