#Define a function for total of list
def sum_list(items):
    sum_number=0
    for i in items:
        sum_number+=i
    return sum_number
#Using the function with an immediate list
print('Total of the list is ',sum_list([7,15,23,4,9,11]))
#Using the function with a defined list
a=[7,15,23,4,9,11]
print('Total of the list ',a,' is ',sum_list(a))