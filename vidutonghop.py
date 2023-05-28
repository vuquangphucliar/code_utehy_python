#Chương trình thực hiện với menu
def ghi_file(f_name):
    txt_file = open(f_name, 'a', encoding='utf-8')
    while (True):
        st_ID = input('Student ID: ')
        if st_ID == "":
            break
        st_name = input('Student name: ')
        st_class = input('Class of student: ')
        st_birthplace = input('Place of birth')
        txt_file.write('\t'.join([st_ID, st_name, st_class, st_birthplace]) + '\n')
    print('Writing complete!')
    txt_file.close()
    return 1
def doc_file(f_name):
    print('List student of all classes')
    print('\t'.join([" ID ", "   Name  ", "  Class  ", "Place of birth"]))
    txt_file = open(f_name, 'r', encoding='utf-8')
    for student in txt_file.readlines():
        print(student,'\t')
    txt_file.close()
    return 1
while True:
    print("1. Nhập danh sách sinh viên vào file ")
    print("2. Đọc dữ liệu sinh viên từ file")
    print("3. Thoát khỏi chương trình")
    chon=int(input("Hãy chọn công việc: "))
    if chon==1:
        ghi_file("a.txt")
    elif chon==2:
        doc_file("a.txt")
    elif chon==3:
         break
    else:
        print("Bạn phải chọn các công việc từ 1 đến 3")