txt_file=open('Student.txt','a',encoding='utf-8')
st_list=[]
while (True):
    st_ID=input('Student ID: ')
    if st_ID=="":
        break
    st_name=input('Student name: ')
    st_class=input('Class of student: ')
    st_birthplace=input('Place of birth')
    txt_file.write('\t'.join([st_ID,st_name,st_class,st_birthplace])+'\n')
print('Writing complete!')
txt_file.close()