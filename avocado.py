# Importing packages
import pandas as pd
import numpy as np

# Importing an advocado dataset as a DataFrame
avocado = pd.read_csv("./data/avocado.csv")

# print(avocado.head())
# print(avocado.describe())
# print(avocado.info())
# print(avocado.values)
# print(avocado.sort_values(["nb_sold", "date", "type"], ascending=[False, False, True]))
# print(avocado[(avocado["size"] == "small") & (avocado["date"] > "2018-01-01")])
# print(avocado)
# def iqr(column):
#     return column.quantile(0.75) - column.quantile(0.25)
# print(avocado[["avg_price", "nb_sold"]].agg([iqr, np.median]))
print(avocado.pivot_table(
    values="avg_price",
    index="year",
    aggfunc=[np.mean, np.max],
    columns="size",
    margins=True,
))