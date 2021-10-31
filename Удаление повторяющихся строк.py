import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe.drop_duplicates().head(2))

print(dataframe.drop_duplicates(subset=["Sex"]).head(2))