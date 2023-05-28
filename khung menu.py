#Viết chương trình sử dụng hàm để tính
# - Tổng các giá trị của danh sách
# - Tìm Min trong danh sách
# Viết dứoi dạng menu
while True:
    print("\t\t 1. Tính tổng")
    print("\t\t 2. Tìm min")
    print("\t\t 3. Thoát")

    c=int(input("Hãy chọn (1,2,3): "))
    if (c==1):
        print("Bạn đã chọn 1")
        #gọi gmaf tính tổng
    elif c==2:
        print("Bạn đã chọn 2")
        #gọi hàm tìm min
    elif c==3:
        break
    else:
        print("Bạn phải chọn 1,2 hoặc 3")