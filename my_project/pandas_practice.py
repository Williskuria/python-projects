import pandas as pd
df = pd.read_csv("people.csv")
print(df.describe())
print(df["age"] > 24)
print(df[df["age"] > 24])