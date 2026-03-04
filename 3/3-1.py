import numpy as np
from scipy.linalg import hilbert, eigvals, svd
import matplotlib.pyplot as plt

for n in [10, 20, 100]:
    A = hilbert(n)
    lambdas = eigvals(A)
    _U, S, _V = svd(A)
    print(f"Matrix {n}, Mean {lambdas.mean().real:.6e}, Min {lambdas.min().real:.6e}, Max {lambdas.max().real:.6e}")
    print(f"SVD values  : mean={S.mean():.6e}, "f"min={S.min():.6e}, max={S.max():.6e} \n")
    #plt.plot(S, 'k-s')
    #plt.show()