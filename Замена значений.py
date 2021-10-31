import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe['Sex'].replace('female', 'Woman').head(2))

# Замена по всему объекту
print(dataframe.replace(1, "One").head(2))