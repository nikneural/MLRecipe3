import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe.head(2))
print(dataframe.shape)
print(dataframe.describe())