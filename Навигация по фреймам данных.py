import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

# Выбрать первую строку
print(dataframe.iloc[0])

dataframe = dataframe.set_index(dataframe["Name"])
print(dataframe.loc["Allen, Miss Elisabeth Walton"])