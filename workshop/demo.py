import pandas as pd
import re

df = pd.read_csv("./part_wine_reviews.csv")
# print(df)

df_5 = df.head(5)
print(df_5)

# 3rd, 4th lines
index = [False, False, True, True, False]
df_filtered = df_5[index]
print(df_filtered)

# description series
ser_descriptions = df_5["description"]
print(ser_descriptions)

# regular expression
index = []
keyword = "aromas"
for description in ser_descriptions:
    if re.search(keyword, description):
        index.append(True)
    else:
        index.append(False)
print(df_5[index])