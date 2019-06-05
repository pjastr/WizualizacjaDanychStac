import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3, 3, 1024)
plt.plot(X, X ** 2, color='k', linestyle='solid')
plt.plot(X, X ** 3 + 22, color='k', linestyle='dashed')
plt.plot(X, X ** 2 - X ** 2, color='k', linestyle='dashdot')
plt.show()
