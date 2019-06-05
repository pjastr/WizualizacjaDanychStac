import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-3, 3, 30)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
plt.annotate('Minimum',
ha = 'center', va = 'bottom',
xytext = (-1.5, 3.),
xy = (0.75, -2.7),
arrowprops = { 'facecolor' : 'green', 'shrink' : 0.05 })
plt.plot(X, Y)
plt.show()