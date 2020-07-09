import numpy as np

def reemplazar_nan(a):
    fallos = np.array(np.isnan(a), dtype=int)
    medias = np.nanmean(a, axis=0)
    b = np.nan_to_num(a) + fallos * medias
    return b

a = np.array([[1,np.nan,3], [4,5,np.nan], [7,8,9]])
print(reemplazar_nan(a))