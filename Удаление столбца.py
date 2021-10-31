import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe.drop("Age", axis=1).head(2))

print(dataframe.drop(["Age", "Sex"], axis=1).head(2))

print(dataframe.drop(dataframe.columns[1], axis=1).head(2))