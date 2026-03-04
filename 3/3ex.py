import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

N = 20
A = np.random.rand(N,N)
U, S, V = np.linalg.svd(A)
print(S)
fig, ax = plt.subplots()
plt.plot(S, 'k-s')
plt.show()