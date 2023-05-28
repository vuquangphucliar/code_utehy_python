Department=['Electronic and Electrical Engineering','Information Technology','Mechanical Engineering',
            'Automobile Engineering','Garment Technology and Fashion Design','Foreign Languages'];
department_ID=['7510301','7480201','7510201','7510202','7540205','7220201'];
table=[];
for x,y in zip(Department,department_ID):
    table.append([x,y])
for i in table:
    print(i)