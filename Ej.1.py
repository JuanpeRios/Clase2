import numpy as np

def expandir(matriz):
    return matriz[:,None]

C = np.array([
    [1,0,0],
    [0,1,0]
])
C_expandida = expandir(C)
X = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
distancia = np.sqrt(np.sum((C_expandida-X)**2,axis=2))
print(distancia)

dist_min = np.argmin(distancia,axis=0)
print(dist_min)
