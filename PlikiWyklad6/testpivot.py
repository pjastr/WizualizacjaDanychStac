import pandas as pd

df = pd.DataFrame({'A': ['John', 'Boby', 'Mina'],
                   'B': ['Masters', 'Graduate', 'Graduate'],
                   'C': [27, 23, 21]})
df2= df.pivot('A', 'B', 'C')
df3=df.pivot(index ='A', columns ='B', values =['C', 'A'])