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

# Series
print(df['country'])

# access a specific element
print(df.iloc[0,3])
df.iloc[0,3] = "Seoul"
print(df.iloc[0,3])

# change the label
print(df.index)
df.index = [f'row_{i}' for i in range(len(df.index))]
print(df.index)