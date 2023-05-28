from pandas import read_csv
import os
from matplotlib import pyplot
path=os.getcwd()+'\data\population.txt'
col=['Population','Profit']
data=read_csv(path,names=col)
data.plot(kind='scatter',x='Population',y='Profit')
pyplot.show()
