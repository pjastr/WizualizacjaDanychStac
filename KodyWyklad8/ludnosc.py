import pandas as pd

data = pd.read_csv("ludnosc.csv", sep=";")

import numpy as np
import matplotlib.pyplot as plt


men= data[data["Płeć"]=="mężczyźni"].iloc[1:,:]
men=men.drop(men.index[-1])
men=men.drop(men.index[-5])
women=data[data["Płeć"]=="kobiety"].iloc[1:,:]
women=women.drop(women.index[-1])
women=women.drop(women.index[-5])
X = np.arange(len(men))
labels = men["Wiek"]
plt.barh(X, women["Wartosc"], color='r', label="Kobiety")
plt.yticks(X,labels)
plt.xticks([-1500000,-1000000,-500000,0,500000,1000000,1500000],["1,5 mln","1 mln","0,5 mln","0 mln","0,5 mln","1 mln", "1,5 mln"])
plt.grid()
plt.barh(X, -men["Wartosc"], color='b', label="Mężczyźni")
plt.legend()
plt.show()
