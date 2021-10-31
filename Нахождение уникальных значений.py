import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe["Sex"].unique())

# Показать количество появлений
print(dataframe["Sex"].value_counts())