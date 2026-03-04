import numpy as np
import matplotlib.pyplot as plt

# Строим равномерную сетку на отрезке [0,1]
l = 1.0
N = 20                      # кол-во интервалов
x = np.linspace(0,l,N+1)    # узлы сетки
h = 1/N                     # шаг сетки

# Сетка по времени
T = 0.1
M = 100
t = np.linspace(0,T,M+1)
tau = T/M

print(tau/h**2)             # для явной схемы < 0.5 

# Условия задачи
f = 0.0
u0 = np.ones_like(x)
mu0 = 1.0
mu1 = 0.0

# Решение в текущий момент времени
u = u0.copy()

# Решение на следующий временной слой
u_hat = np.zeros_like(x)

fig, ax = plt.subplots()

# Явная схема
for s in range(1,M+1):
	for i in range(1,N):
		u_hat[i] = u[i] + tau/h**2 * (u[i-1] - 2*u[i] + u[i+1]) + tau*f
	u_hat[0] = mu0
	u_hat[-1] = mu1
	u = u_hat.copy()

	if s % 10 == 0:
		plt.plot(x, u_hat, label=fr'$t={t[s]}$')

plt.legend()
plt.show()