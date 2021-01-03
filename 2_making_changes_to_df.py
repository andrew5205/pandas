


import pandas as pd
import numpy as np

df = pd.read_csv('pokemon_data.csv')


# Make changes to DataFrame

# print(df.columns)

# df.head(5)
# print(df.head(5))

# ******************************************************************************************************
# # # add a column
# # # add a column 'Total' is the sum of all numbers 
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# # print(df.head(5))

# # print(df.iloc[1])
# print(df.iloc[:4])
# #    #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  Total
# # 0  1              Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False    318
# # 1  2                Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False    405
# # 2  3               Venusaur  Grass  Poison  80      82       83      100      100     80           1      False    525
# # 3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False    625


# ******************************************************************************************************
# # remove a column
# # will not directly change to original df 
# df = df.drop(columns= ['Total'])
# print(df.iloc[:4])


# ******************************************************************************************************
# better way to add a column 

# # .iloc[:,] - :, means all rows 

# df['total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df.iloc[:4])
# #     #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  total
# # 0  1              Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False    318
# # 1  2                Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False    405
# # 2  3               Venusaur  Grass  Poison  80      82       83      100      100     80           1      False    525
# # 3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False    625  

# ******************************************************************************************************

# rearange columns orders
# make original columns into a new list, then concat
df['total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# cols[-1] is a str 
# [cols[-1]] is a list element

# print(df.iloc[:4])
#    #                   Name Type 1  Type 2  total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0  1              Bulbasaur  Grass  Poison    318  45      49       49       65       65     45           1      False
# 1  2                Ivysaur  Grass  Poison    405  60      62       63       80       80     60           1      False
# 2  3               Venusaur  Grass  Poison    525  80      82       83      100      100     80           1      False
# 3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123      122      120     80           1      False




