import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

plt.style.use('dark_background')

# Make data
step = 0.01
w = 5
X = np.arange(-w, w + step, step)
Y = np.arange(-w, w + step, step)
X, Y = np.meshgrid(X, Y)
Q = 0.5 * (Y + (1 + X) * Y - np.abs(Y - (1 + X) * Y))
Z = 0.5 * (Q + (1 - X) * Y + np.abs(Q - (1 - X) * Y))


# Plot the contours

fig, ax = plt.subplots()

cont = ax.contourf(X, Y, Z, cmap=cm.Spectral, levels=100)

# Add a color bar which maps values to colors.
fig.colorbar(cont, shrink=0.5, aspect=5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Max(Min(Y,(1+X)*Y),(1-X)*Y)')
plt.tight_layout()


plt.savefig('../images/2024-02-xx-max-min-example.png', dpi=300, transparent=True)
plt.close()
