import numpy as np
import matplotlib.pyplot as plt

# Строим равномерную сетку на отрезке [0,1]
l = 1.0
N = 10                      # кол-во интервалов
x = np.linspace(0,l,N+1)    # узлы сетки
h = 1/N                     # шаг сетки

# Сетка по времени
T = 1.0
M = 100
t = np.linspace(0,T,M+1)
tau = T/M
#print(tau/h**2)

k = 1.0
q = 0.1
f = 1.0
#𝑢(𝑥,0)=0 , 𝑥∈[0,1]
u0 = np.zeros(N + 1)
#2 : u(0,t)=0,  ∂u∂n(1,t)+u(1,t)=t, 0<t≤1
mu0 = 0.0
#mu1 = 1.0
u = u0.copy()
u_hat = np.zeros_like(u)

u_mid = [u[N//2]]

r = tau / h**2
A = np.zeros((N, N))
for j in range(N-1):
    A[j, j] = 1 + tau*q + 2*r
    if j > 0:
        A[j, j-1] = -r
    if j < N-1:
        A[j, j+1] = -r
#A[N-1, N-2] = -1.0 / h
#A[N-1, N-1] = 1.0 / h + 1.0
A[N-1, N-2] = -2*r
A[N-1, N-1] = 1+2*r+tau*q+2*h*r

for s in range(1, M+1):
    b = np.zeros(N)
    b[0:N-1] = u[1:N] + tau*f
    
    b[-1] = u[N] + tau*f + 2*h*r * t[s]
    u_hat[1:N+1] = np.linalg.solve(A, b)
    
    u_hat[0] = mu0
    u_mid.append(u_hat[N//2])
    u = u_hat.copy()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, u, color='blue')
ax1.grid(True)
ax2.plot(t, u_mid, color='red')
ax2.grid(True)
plt.show()