import numpy as np
import matplotlib.pyplot as plt

n = 80
h = 1.0 / (n + 1)
x = np.linspace(h, 1-h, n)
f_true = np.zeros(n)
f_true[x > 0.5] = 1.0
A  = np.zeros((n, n))
for i in range(n):
    if i > 0:
        A[i][i-1] = -1 / h**2
    if i < n-1:
        A[i][i+1] = -1 / h**2
    A[i][i] = 2 / h**2
#print(D)
u = np.linalg.solve(A, f_true)
u_delta = u + 0.0001 * np.random.normal(0, 1, n)

D = np.zeros((n-1, n))
for i in range(len(D)):
    D[i, i]   =  1.0 / h          #!?
    D[i, i+1] = -1.0 / h         #!?

alpha = 1e-3
f_tikh = np.linalg.solve(np.eye(n) + alpha*(D.T @ D), A @ u_delta)


tau = 0.02
eps = 1e-6
max_iter = 50000
D_inv = np.linalg.inv(A)

f_k = np.ones(n)
for _ in range(max_iter):
    f_new = f_k + tau * (D_inv @ (A @ u_delta - f_k))
    if np.linalg.norm(f_new - u) < eps:
        print("F.")
        break
    f_k = f_new
print(f"t ITER: {_+1}")


plt.figure(figsize=(9,4))
plt.step(x, f_true, label='Exact', linewidth=2)
plt.plot(x, f_tikh, label=f'Tikhonov', linewidth=2)
plt.plot(x, f_k, label=f'Prostoy iter', linewidth=2)
plt.xlabel('x')
plt.legend()
plt.grid(True)
plt.show()