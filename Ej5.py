import numpy as np

def variable_exponencial(lam,n):
    U = np.random.uniform(0, 1, n)
    X = -(np.log(1 - U)) / lam
    return X

print(variable_exponencial(1,10))