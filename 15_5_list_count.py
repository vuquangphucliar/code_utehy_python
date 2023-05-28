#Count number elements of a list
l=[121,45,454,67,232,89,233,771,33,200]
def l_count(list):
    c=0
    for i in list:
        c+=1
    return(c)
print(l_count(l))