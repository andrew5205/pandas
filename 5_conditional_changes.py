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

# df.loc[condition, columns] = variable
df.loc[df['Type 1'] == 'Grass', 'Type 1'] = 'Flamer'
# print(df.head(5))
# # #   #                   Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# # 0  1              Bulbasaur  Flamer  Poison  45      49       49       65       65     45           1      False
# # 1  2                Ivysaur  Flamer  Poison  60      62       63       80       80     60           1      False
# # 2  3               Venusaur  Flamer  Poison  80      82       83      100      100     80           1      False
# # 3  3  VenusaurMega Venusaur  Flamer  Poison  80     100      123      122      120     80           1      False
# # 4  4             Charmander    Fire     NaN  39      52       43       60       50     65           1      False


# ******************************************************************************************************

# just to get back to orginal csv file 
df = pd.read_csv('pokemon_data.csv')



# also can change multiple columns at the same time  

df.loc[df['Type 1'] == 'Grass', ['Generation', 'Legendary']] = ['100', 'True']
# print(df.head(10))
# #     #                       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed Generation Legendary
# # 0  1                  Bulbasaur  Grass  Poison  45      49       49       65       65     45        100      True
# # 1  2                    Ivysaur  Grass  Poison  60      62       63       80       80     60        100      True
# # 2  3                   Venusaur  Grass  Poison  80      82       83      100      100     80        100      True
# # 3  3      VenusaurMega Venusaur  Grass  Poison  80     100      123      122      120     80        100      True
# # 4  4                 Charmander   Fire     NaN  39      52       43       60       50     65          1     False
# # 5  5                 Charmeleon   Fire     NaN  58      64       58       80       65     80          1     False
# # 6  6                  Charizard   Fire  Flying  78      84       78      109       85    100          1     False
# # 7  6  CharizardMega Charizard X   Fire  Dragon  78     130      111      130       85    100          1     False
# # 8  6  CharizardMega Charizard Y   Fire  Flying  78     104       78      159      115    100          1     False
# # 9  7                   Squirtle  Water     NaN  44      48       65       50       64     43          1     False














