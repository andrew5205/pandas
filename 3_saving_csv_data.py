

# df.to_csv()


import pandas as pd
import numpy as np

df = pd.read_csv('pokemon_data.csv')

# print(df.columns)

# df.head(5)
# print(df.head(5))
# #    #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# # 0  1              Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False
# # 1  2                Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False
# # 2  3               Venusaur  Grass  Poison  80      82       83      100      100     80           1      False
# # 3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False
# # 4  4             Charmander   Fire     NaN  39      52       43       60       50     65           1      False

# ******************************************************************************************************
# add column 'Total, save to modified.csv
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.iloc[:4])

df.to_csv('modified.csv')
#    #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  Total
# 0  1              Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False    318
# 1  2                Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False    405
# 2  3               Venusaur  Grass  Poison  80      82       83      100      100     80           1      False    525
# 3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False    625



# remove index while saving 
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.iloc[:4])

df.to_csv('modified_index_free.csv', index= False)
# df.to_csv('modified_index_free.xlsx', index= False)
df.to_csv('modified_index_free.txt', index= False, sep='\t')


# ******************************************************************************************************















