import pandas as pd

st_file=pd.read_csv('Student.txt',sep='\t',header=None,names=["ID","Name","Class","Place of birth"])
print('List students of all classes\n',st_file)
class_st=st_file['Class'].unique()
writer= pd.ExcelWriter('student.xlsx')
for cl in class_st:
    print(cl)
    class_of_student=st_file.query('Class == @cl')
    print(class_of_student)
    class_of_student.to_excel(writer,str(cl),index=False)
writer.save()