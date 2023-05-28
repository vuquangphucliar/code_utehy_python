from pandas import read_csv
import os

path=os.getcwd()+'\data\iris.csv'
col=['Sepal length','Sepan width','Sepal length','Sepan width','Class']
data=read_csv(path,names=col)

print(data.shape)       #Show number of columns and number of rows
print(len(data))        #Show length of data
print(data)             #Print all data
print(data.head())      #Print five first rows (default)
print(data.head(10))    #Print ten first rows
print(data.tail(3))     #Print three endding rows
