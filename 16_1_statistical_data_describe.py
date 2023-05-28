from pandas import read_csv
import os

path=os.getcwd()+'\data\iris.csv'
col=['Sepal length','Sepan width','Sepal length','Sepan width','Class']
data=read_csv(path,names=col)
#Describe for all features
print(data.describe())
print('Describe for feature \"Sepal length"',data['Sepal length'].describe())
#Correlation of data
print(data.corr(method='pearson',min_periods=1))