import pandas as pd
import numpy as np

time_index = pd.date_range("06/06/2017", periods=100000, freq='30S')

dataframe = pd.DataFrame(index=time_index)

dataframe["Sale_Amount"] = np.random.randint(1, 10, 100000)

print(dataframe.resample("W").sum())