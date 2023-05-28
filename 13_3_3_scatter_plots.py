#Have to install package plotting
from pandas import read_csv
import os
from matplotlib import pyplot
from pandas.plotting  import scatter_matrix
path=os.getcwd()+'\data\iris.csv'
col=['Sepal length 1','Sepal width 1','Sepal length 2','Sepal width 2','Variety']
data=read_csv(path,names=col)
scatter_matrix(data)
pyplot.show()