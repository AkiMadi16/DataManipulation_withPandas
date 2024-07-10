# Welcome to my Coding Journey on Data Manipulation with pandas

Hello there! 👋🏽 

# What You'll Find Here 🦾

In this repository, I'm documenting my journey of learning and experimenting with code.

# Power Bi Dashboard
![Dashboard](DataManipulation_withPandas)

# Let's start exploring data

When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. The following code cells show useful methods and attributes for this.
![first Rows](https://www.datacamp.com/datalab/w/56af03e9-ef4f-43ea-86f4-6c599617e82b/edit)


### Return the first few rows of a DataFrame
```diff
+ print(avocado.head())
```

![first Rows](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.16.44%E2%80%AFam.png)

### Compute some summary statistics for numerical columns

```diff
+ print(avocado.describe())
```

![Summary stats](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.17.58%E2%80%AFam.png)

### Print the names of columns, the data types they contain, and whether they have any missing values

```diff
+ print(avocado.info())
```
![missing values](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.18.17%E2%80%AFam.png)

### Return the data values in a 2D NumPy array

```diff
+ print(avocado.values)
```

### Sort by multiple variables by passing lists of column names and booleans

```diff
+ print(avocado.sort_values(["nb_sold", "date", "type"], ascending=[False, False, True]))
```
![sorting](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.18.41%E2%80%AFam.png)

```diff
+ print(avocado[(avocado["size"] == "small") & (avocado["date"] > "2018-01-01")])
```
![sort by size & date](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.19.02%E2%80%AFam.png)


```diff
+ print(avocado)
```
![data](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.19.32%E2%80%AFam.png)

### The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than one column of a DataFrame at once.

### Define a custom function: this one computes the inter-quartile range (IQR)

```diff
  def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
```
### Apply multiple functions

```diff
+ print(avocado[["avg_price", "nb_sold"]].agg([iqr, np.median]))
```

![agg method](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.21.35%E2%80%AFam.png)

### Pivot tables are another way of calculating grouped summary statistics. The .pivot_table() method has:

a values argument which takes the name of the column you want to summarize.
an index argument which takes the name of the column you want to group by.
an aggfunc argument which takes in a list of functions to summarize the values. By default, .pivot_table() uses the mean.
a columns argument which takes in the name of any other columns you want to group by.
a fill_value argument to define what should replace missing values.
a margins argument. Setting this to True enables summary statistics for multiple levels of the dataset.

```diff
  print(avocado.pivot_table(
    values="avg_price",
    index="year",
    aggfunc=[np.mean, np.max],
    columns="size",
    margins=True,
))
```

![pivot table](https://github.com/AkiMadi16/DataManipulation_withPandas/blob/main/output_images/Screenshot%202024-06-14%20at%205.21.46%E2%80%AFam.png)