import sys

import numpy as np
observedfile = sys.argv[1]
predictedfile = sys.argv[2]

X = np.loadtxt(observedfile,delimiter=",",dtype=str,skiprows=1)
Y = np.loadtxt(predictedfile,delimiter=",",dtype=str,skiprows=1)

print("Correlation (r): ")
print(np.corrcoef(X[:,1].astype('float64'), Y[:,1].astype('float64'))[1,0])

print("RMSE: ")
print(np.sqrt(np.mean((X[:,1].astype('float64') - Y[:,1].astype('float64'))**2)))
