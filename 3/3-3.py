import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import hilbert, eigvals, svd

n = 20
delta = 0.05
A = hilbert(n)
x_exact = np.ones(n)

b = A @ x_exact
sigma = np.random.normal(0, 1, n)
print(sigma)
b_delta = b + delta * sigma
alphas = np.logspace(-8,-2,100)

I_vals = []
graph2_vals = []
graph3_vals = []
graph4_vals = []

for alpha in alphas:
    x = np.linalg.solve(A.T @ A + alpha*np.eye(n), A.T @ b_delta)
    I = np.linalg.norm(A @ x - b_delta)**2 + alpha*np.linalg.norm(x)**2
    I_vals.append(I)
    graph2_vals.append(np.linalg.norm(A @ x - b_delta)**2)
    graph3_vals.append(alpha*np.linalg.norm(x)**2)
    graph4_vals.append(np.linalg.norm(x_exact - x)**2)

fig, ax = plt.subplots(2,2, figsize=(12,8))
line = n * delta**2

ax[0,0].semilogx(alphas, I_vals)
ax[0,0].axhline(line, linestyle="--", label="line")
ax[0,0].set_title("J(x_alpha)")
ax[0,0].grid()

ax[0,1].semilogx(alphas, graph2_vals)
ax[0,1].axhline(line, linestyle="--", label="line")
ax[0,1].set_title("norm(A*x-b_delta)**2")
ax[0,1].legend()
ax[0,1].grid()

ax[1,0].semilogx(alphas, graph3_vals)
ax[1,0].axhline(line, linestyle="--", label="line")
ax[1,0].set_title("a*norm(x)**2")
ax[1,0].grid()

ax[1,1].semilogx(alphas, graph4_vals)
ax[1,1].axhline(line, linestyle="--", label="line")
ax[1,1].set_title("norm(x_exact-x)**2")
ax[1,1].grid()

plt.tight_layout()
plt.show()