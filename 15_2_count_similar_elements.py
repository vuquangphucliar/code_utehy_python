L=[1,5,6,3,8,1,9,4,3,1,6]
x=int(input('Enter a number: '))
def sim_count(source_list):
    c=0
    for i in source_list:
        if x==i:
            c+=1
    return c
for i in L:
    print(i,end='\t')
if sim_count(L)==0:
    print('\nDon\'t find anny elements of list equal to ',x)
else:
    print('\nHave ',sim_count(L),' elements of list equal to ', x)