import pandas as pd

df = pd.DataFrame({'Name': {0: 'John', 1: 'Bob', 2: 'Shiela'},
                   'Course': {0: 'Masters', 1: 'Graduate', 2: 'Graduate'},
                   'Age': {0: 27, 1: 23, 2: 21}})

df2= pd.melt(df, id_vars=['Name'], value_vars=['Course'])
df3=pd.melt(df, id_vars=['Name'], value_vars=['Course', 'Age'])
df4=pd.melt(df, id_vars=['Name'], value_vars=['Course'],
        var_name='ChangedVarname', value_name='ChangedValname')
