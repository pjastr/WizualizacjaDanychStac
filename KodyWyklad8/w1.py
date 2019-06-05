import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(500, 2)
plt.scatter(data[:, 0], data[:, 1])
plt.show()
