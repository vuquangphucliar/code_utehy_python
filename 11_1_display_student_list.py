print('List student of all classes')
print('\t'.join(["   ID ","          Name  ","       Class  ","     Place of birth"]))

txt_file=open('Student.txt','r',encoding='utf-8')
for student in txt_file.readlines():
    print(student)
txt_file.close()

print('List students of the class 123')
print('\t'.join([" ID ","   Name  ","  Class  ","Place of birth"]))
txt_file=open('Student.txt','r',encoding='utf-8')
for student in txt_file.readlines():
    if student.find("110194")>=0:
        print(student)
txt_file.close()