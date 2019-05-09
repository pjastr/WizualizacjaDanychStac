import pandas as pd

data = pd.read_csv('jajka2.csv', sep=';', index_col=0)
data2 = data.stack()
data3 = data2.str.replace(',', '.').astype('float')

srednia = data3.mean()

minCena = data3.min()
maxCena = data3.max()
lokMin = data3[data3 == minCena]
lokMax = data3[data3 == maxCena]
