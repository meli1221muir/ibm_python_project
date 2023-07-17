from ast import increment_lineno
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file from path above and assign it to variable "df"
df = pd.read_csv("C:/Users/Melania Muir/Desktop/Python/imports-85.csv", header=None)

# create a Python list headers containing name of headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# replace headers 
df.columns = headers

# Write your code below and press Shift+Enter to execute 
#df['peak-rpm'].dtypes

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)

# Convert data types to proper format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("float")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1

# create pivot table
#grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
#grouped_pivot

#grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
#grouped_pivot

#use the grouped results
#plt.pcolor(grouped_pivot, cmap='RdBu')
#plt.colorbar()

# add labels
#fig, ax = plt.subplots()
#im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
#row_labels = grouped_pivot.columns.levels[1]
#col_labels = grouped_pivot.index

#move ticks and labels to the center
#ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
#ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
#ax.set_xticklabels(row_labels, minor=False)
#ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
#plt.xticks(rotation=90)

#fig.colorbar(im)
#plt.show()

# plot box and whiskers chart
sns.boxplot(x="body-style", y="price", data=df)
plt.show()