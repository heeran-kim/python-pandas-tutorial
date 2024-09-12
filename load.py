import pandas as pd

df = pd.read_csv(r"/Users/lani/Documents/Griffith University/2024 T2/7810ICT - Software Technologies/project/workshop8/workshop/part_wine_reviews.csv")
# The r in Python is a raw string prefix.
# It tells Python to treat backslashes (\) as literal characters,
# rather than escape characters.

print(df.index) # RangeIndex(start=0, stop=299, step=1)
print(*df.index)

print(df.columns)
# Index(['country', 'points', 'price', 'province', 'region', 'variety', 'winery',
#        'description'],
#       dtype='object')

# Series: Select a column by a column label
print(df['country'])

# access a specific element
print(df.iloc[0,3])
df.iloc[0,3] = "Seoul"
print(df.iloc[0,3])

# change the label
print(df.index)
df.index = [f'row_{i}' for i in range(len(df.index))]
print(df.index)

# Select a row by a row label
print(df.loc['row_0'])

# Selecting all rows (:) with column labels
print(df.loc[:, ['country', 'points']])

# Select a row by row's position
print(df.iloc[3])

# Select multiple rows by slices
print(df.iloc[0:3])

# select a sub-grid by row & colum slices
print(df.iloc[2:5, 1:3])

# select a sub-grid by specific positions
print(df.iloc[[0,2,3], [1,7]])

#
print(df[df["price"] < 10].loc[:, ['price']])

# randomly pick rows
import numpy as np
bool_ind = np.random.random((299,))
print(bool_ind)
bool_idx = bool_ind > 0.5
print(bool_idx)
new_df = df[bool_idx]
print(new_df)