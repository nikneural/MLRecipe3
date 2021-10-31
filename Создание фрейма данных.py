import pandas as pd

dataframe = pd.DataFrame()

dataframe["Имя"] = ['Джеки Джексон', 'Стивен Стивенсон']
dataframe['Возраст'] = [38, 25]
dataframe["Водитель"] = [True, False]

print(dataframe)

new_person = pd.Series(["Молли Муни", 40, True], index=['Имя', 'Возраст', 'Водитель'])

print(dataframe.append(new_person, ignore_index=True))
