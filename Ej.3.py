import numpy as np

def k_means(X,n):
    centroides = np.eye(n, np.shape(X)[1])
    exp_cent = centroides[:, None]

    ### CALCULA LOS NUEVOS CENTROIDES
    distancia = np.sqrt(np.sum((exp_cent - X) ** 2, axis=2))
    dist_min = np.argmin(distancia, axis=0)
    for i in range(n):
        centroides[i] = np.mean(X[dist_min == i, :], axis=0)
    return centroides,dist_min

iteraciones = 10  # Cantidad de iteraciones
n = 4 #Numero de clusters
X = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
])

### SE CREA EL DATASET SINTETICO
X = np.repeat(X,iteraciones,axis=0)
ruido = np.random.normal(0,1,np.shape(X))
X = X + 0.2*ruido #Realizaciones de la V.A.

centroides, dist_min = k_means(X,n)

print("Los centroides son:\n",centroides)
print("Las realizaciones pertenecen a los centroides:\n",dist_min)

