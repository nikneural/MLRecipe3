import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print("Максимум: {}".format(dataframe["Age"].max()))
print("Минимум: {}".format(dataframe["Age"].min()))
print("Среднее: {}".format(dataframe["Age"].mean()))
print("Сумма: {}".format(dataframe["Age"].sum()))
print("Количество: {}".format(dataframe["Age"].count()))
print("Медиана: {}".format(dataframe["Age"].median()))