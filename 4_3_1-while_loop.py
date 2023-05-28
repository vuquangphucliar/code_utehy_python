# #FEE - Faculty of Electronic and Electrical Engineering
# #FIT - Faculty of Information Technology
# #FME - Faculty of Mechanical Engineering
# #FAE - Faculty of Automobile Engineering
# #FGTFD - Faculty of Garment Technology and Fashion Design
# #FFL - Faculty of Foreign Languages
# collection=['Electronic and Electrical Engineering','Information Technology','Mechanical Engineering',
#             'Automobile Engineering','Garment Technology and Fashion Design','Foreign Languages']
            
# print()
# print(' Hung Yen University of Technology and Education is a medium university in Vietnam. There are a lot of faculties in HYUTE, including, ');
# i=0
# while i < len(collection):
#     print('\t',i+1, '.  Faculty of ',collection[i] ,'\n');
#     i+=1;
num=int(input('Nhập N : '))
i=1
tich=1
while (i<num+1):
    tich=tich*i
    i+=1;
print(tich)