import numpy as np
from scipy.linalg import hilbert, eigvals, svd
import matplotlib.pyplot as plt

n = 20
eps = 1e-6

A = hilbert(n)
x_exact = np.ones(n)
b = A @ x_exact
b_delta = b + 0.05 * np.random.normal(0, 1, n)
print(b)
print(b_delta)
A = A.T @ A
b_delta = A.T @ b_delta
_, S, _ = svd(A)
lambda_max = S.max()
tau = 1 / lambda_max

u = np.zeros(n)
for _ in range(1000000):
    u_new = u + tau * (b_delta - A @ u)
    if np.linalg.norm(u_new - u) < eps:
        print("F.")
        break
    u = u_new
print(u)
print(f"t ITER: {_+1}")
alpha = 1e-6
x = np.linalg.solve(A.T @ A + alpha*np.eye(n), A.T @ b_delta)
fig, ax = plt.subplots()
plt.plot(u, 'k-s', label="prostoy iter")
plt.plot(x, 'b', label="tihonov")
plt.legend()
plt.show()