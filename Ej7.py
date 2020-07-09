import numpy as np

def z_score(X,n,m):
    mu = np.mean(X, axis=1)
    mu = mu[:, None]
    sigma = np.std(X, axis=1)
    sigma = sigma[:, None]
    Z = (X - mu) / sigma
    return Z

n = 6
m = 6
X = np.random.normal(3,5,(n,m))
print(z_score(X,n,m))

