st_list=[]
while (True):
    st_ID=input('Student ID: ')
    if st_ID=="":
        break
    st_name=input('Student name: ')
    st_class=input('Class of student: ')
    st_birthplace=input('Place of birth')
    st_list.append([st_ID,st_name,st_class,st_birthplace])
print('List of the class:........')
print(f'Student ID  Name    Class  Place of birth')
for student in st_list:
    print('\t'.join(student))