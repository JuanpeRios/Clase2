import numpy as np
import sklearn
#from sklearn.preprocessing import StandardScaler

X = np.array([[0.4, 4800, 5.5], [0.7, 12104, 5.2], [1, 12500, 5.5], [1.5, 7002, 4.0]])
centrado = X - np.mean(X,axis=0)
covarianza = np.cov(centrado.T)
W,V = np.linalg.eig(covarianza)
ordenar = np.argsort(W)[::-1]
V_ordenado = V[ordenar]
d = 2
PCA_1 = np.matmul(centrado,V_ordenado[:,:d])
print(PCA_1)

