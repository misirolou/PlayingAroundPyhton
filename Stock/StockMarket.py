#Another way of trying out analyzing info from a CSV file
# https://nicholastsmith.wordpress.com/2016/04/20/stock-market-prediction-using-multi-layer-perceptrons-with-tensorflow/

import numpy as np 
#pip install TFANN
#from TFANN import ANNR 
import matplotlib.pyplot as mpl 
from sklearn.preprocessing import scale

pth = 'Stock\MSFT.csv'
A = np.loadtxt(pth, delimiter=",", skiprows=1, usecols=(1,4))
A = scale(A)

y = A[:,1].reshape(-1,1)

A = A[:,0].reshape(-1,1)

mpl.plot(A[:,0], y[:,0])
mpl.show()