#FEE - Faculty of Electronic and Electrical Engineering
#FIT - Faculty of Information Technology
#FME - Faculty of Mechanical Engineering
#FAE - Faculty of Automobile Engineering
#FGTFD - Faculty of Garment Technology and Fashion Design
#FFL - Faculty of Foreign Languages
collection=['Electronic and Electrical Engineering','Information Technology','Mechanical Engineering',
            'Automobile Engineering','Garment Technology and Fashion Design','Foreign Languages'];
print(' Hung Yen University of Technology and Education is a medium university in Vietnam. There are a lot of faculties in HYUTE, including, ');
for i in range(len(collection)):
    print('\t',i+1,' Faculty of ',collection[i] ,'\n')
    