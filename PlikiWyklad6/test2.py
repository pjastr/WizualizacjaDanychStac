import pandas as pd

df = pd.read_csv("f500.csv")

df = pd.read_csv("f500.csv", header=0)
df = pd.read_csv("f500.csv", header=1)
df = pd.read_csv("f500.csv", header=None)
df = pd.read_csv("f500.csv", names=["COL1", "COL2", "COL3", "COL4", "COL5", "COL6",
                                    "COL7", "COL8", "COL9", "COL10", "COL11", "COL12",
                                    "COL13", "COL14", "COL15", "COL16", "COL17", "COL18"])
df = pd.read_csv("f500.csv", header=None, prefix='COL')
df = pd.read_csv("f500.csv", index_col=0)
df = pd.read_csv("f500.csv", index_col=[0, 1])
df = pd.read_csv("f500.csv", index_col=["company", "rank"])
df = pd.read_csv("f500.csv", usecols=["company", "rank", "revenues"])
df = pd.read_csv("f500.csv", usecols=[0, 1, 2])
df = pd.read_csv("f500.csv", usecols=["company", "rank", "revenues"])
df = pd.read_csv("f500.csv", dtype={"revenues": "float64"})
df = pd.read_csv("f500.csv", skiprows=2)
df = pd.read_csv("f500.csv", skiprows=[2, 3, 4])
