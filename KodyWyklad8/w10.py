import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3, 3, 20)
Y1 = np.sinc(X)
Y2 = np.sinc(X) + 1
plt.plot(X, Y1, marker='<', color='blue')
plt.plot(X, Y2, marker='o', color='green')
plt.show()
