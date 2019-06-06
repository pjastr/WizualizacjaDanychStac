import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 50)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
box = {
    'facecolor': 'yellow',
    'edgecolor': 'green',
    'boxstyle': 'round'
}
plt.text(0.4, -0.20, 'Minimum', bbox=box)
plt.plot(X, Y, c='k')
plt.show()
