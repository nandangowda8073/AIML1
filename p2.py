import pandas as pd
data = pd.read_csv("C:/Users/SPTINT-07/Desktop/dataset/character.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data["Survival Ability"])
print(data.describe())
print(data["Gender"])
print(data.info())
print(data.dtypes)
print(data.count())

