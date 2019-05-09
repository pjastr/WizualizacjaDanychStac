import pandas as pd

df = pd.read_csv('plik1.csv', sep=";", header=None, index_col=0)
print(df)

print(df.size)