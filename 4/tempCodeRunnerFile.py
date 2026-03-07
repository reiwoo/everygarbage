ax

#lambda_max = np.max(eigvals)

#tau = 1 / lambda_max

## начальное приближение
#u = np.zeros(n)

#k = 0

#while True:

#    u_new = u + tau * (b_delta - A @ u)

#    if np.linalg.norm(u_new - u) < eps:
#        break

#    u = u_new
#    k += 1

#print("число итераций =", k)
#print("решение =", u_new)