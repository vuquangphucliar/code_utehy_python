import pandas as pd

st_file=pd.read_csv('Student.txt',sep="\t",header=None,names=[" ID ","Name","Class","Place of birth"])
print('List students of all classes\n',st_file)
