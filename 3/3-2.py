import numpy as np
import matplotlib.pyplot as plt

n = 20
delta = 0.05
A = np.random.rand(n, n)
b_ = np.random.rand(n) + 0.05 * np.random.randn(n)

x = np.linalg.solve(A, b_)
print(b_)
print(x)
cond = np.linalg.cond(A)
print(" "*100+str(cond))
fig, ax = plt.subplots()
plt.plot(b_, 'k-s', label="shum")
plt.plot(x, 'b')
plt.legend()
plt.show()