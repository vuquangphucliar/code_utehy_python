#Have to install package 'spicy'
from pandas import read_csv
import os
from matplotlib import pyplot

path=os.getcwd()+'\data\iris.csv'
col=['Sepal length 1','Sepal width 1','Sepal length 2','Sepal width 2','Variety']
data=read_csv(path,names=col)
data.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
pyplot.show()