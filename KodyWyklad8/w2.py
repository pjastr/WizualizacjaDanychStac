import matplotlib.pyplot as plt

data = [5., 33., 50., 12.]
plt.barh(range(len(data)), data)
plt.show()
