import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)


def uppercase(x: str) -> str:
    return x.upper()


print(dataframe["Name"].apply(uppercase)[0:2])
