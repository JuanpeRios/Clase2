import numpy as np

def filtrar_filas(a):
    b = np.argwhere(np.isnan(a).any(axis=1) == False)
    return (a[b])

def filtrar_columnas(a):
    b = np.argwhere(np.isnan(a).any(axis=0) == False)
    return (a[:,b])

a = np.array([[1,2,3], [4,5,np.nan], [7,8,9]])
print(filtrar_filas(a))
print(filtrar_columnas(a))