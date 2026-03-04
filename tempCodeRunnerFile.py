fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x, u[-1, :])
axes[1].plot(np.linspace(0, T, Nt+1), u_)

plt.show()