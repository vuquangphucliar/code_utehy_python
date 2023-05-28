Department=('Electronic and Electrical Engineering','Information Technology','Mechanical Engineering',
            'Automobile Engineering','Garment Technology and Fashion Design','Foreign Languages');
department_ID=('7510301','7480201','7510201','7510202','7540205','7220201');
nested_tuple=[];
for x,y in zip(Department,department_ID):
    nested_tuple.append([x,y])
for i in nested_tuple:
    print(i)