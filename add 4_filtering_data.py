
# df.loc[] - Access a group of rows and columns by label(s) or a boolean array.

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

Grass = df.loc[df['Type 1'] == 'Grass']
print(Grass)
#        #                   Name Type 1    Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0      1              Bulbasaur  Grass    Poison   45      49       49       65       65     45           1      False
# 1      2                Ivysaur  Grass    Poison   60      62       63       80       80     60           1      False
# 2      3               Venusaur  Grass    Poison   80      82       83      100      100     80           1      False
# 3      3  VenusaurMega Venusaur  Grass    Poison   80     100      123      122      120     80           1      False
# 48    43                 Oddish  Grass    Poison   45      50       55       75       65     30           1      False
# ..   ...                    ...    ...       ...  ...     ...      ...      ...      ...    ...         ...        ...
# 718  650                Chespin  Grass       NaN   56      61       65       48       45     38           6      False
# 719  651              Quilladin  Grass       NaN   61      78       95       56       58     57           6      False
# 720  652             Chesnaught  Grass  Fighting   88     107      122       74       75     64           6      False
# 740  672                 Skiddo  Grass       NaN   66      65       48       62       57     52           6      False
# 741  673                 Gogoat  Grass       NaN  123     100       62       97       81     68           6      False

# [70 rows x 12 columns]


# ******************************************************************************************************
Type_1_2 = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
# Type_1_2 = df.loc[(df['Type 1'] == 'Grass') and (df['Type 2'] == 'Poison')]     # ValueError: The truth value of a Series is ambiguous
print(Type_1_2)

#        #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0      1              Bulbasaur  Grass  Poison   45      49       49       65       65     45           1      False
# 1      2                Ivysaur  Grass  Poison   60      62       63       80       80     60           1      False
# 2      3               Venusaur  Grass  Poison   80      82       83      100      100     80           1      False
# 3      3  VenusaurMega Venusaur  Grass  Poison   80     100      123      122      120     80           1      False
# 48    43                 Oddish  Grass  Poison   45      50       55       75       65     30           1      False
# 49    44                  Gloom  Grass  Poison   60      65       70       85       75     40           1      False
# 50    45              Vileplume  Grass  Poison   75      80       85      110       90     50           1      False
# 75    69             Bellsprout  Grass  Poison   50      75       35       70       30     40           1      False
# 76    70             Weepinbell  Grass  Poison   65      90       50       85       45     55           1      False
# 77    71             Victreebel  Grass  Poison   80     105       65      100       70     70           1      False
# 344  315                Roselia  Grass  Poison   50      60       45      100       80     65           3      False
# 451  406                  Budew  Grass  Poison   40      30       35       50       70     55           4      False
# 452  407               Roserade  Grass  Poison   60      70       65      125      105     90           4      False
# 651  590                Foongus  Grass  Poison   69      55       45       55       55     15           5      False
# 652  591              Amoonguss  Grass  Poison  114      85       70       85       80     30           5      False


# ******************************************************************************************************

filtered = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print(filtered)
#        #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 2      3               Venusaur  Grass  Poison   80      82       83      100      100     80           1      False
# 3      3  VenusaurMega Venusaur  Grass  Poison   80     100      123      122      120     80           1      False
# 50    45              Vileplume  Grass  Poison   75      80       85      110       90     50           1      False
# 77    71             Victreebel  Grass  Poison   80     105       65      100       70     70           1      False
# 652  591              Amoonguss  Grass  Poison  114      85       70       85       80     30           5      False

# filtered.to_csv('filtered.csv')



# ******************************************************************************************************
new_df = filtered.reset_index()
print(new_df)
#    index    #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0      2    3               Venusaur  Grass  Poison   80      82       83      100      100     80           1      False
# 1      3    3  VenusaurMega Venusaur  Grass  Poison   80     100      123      122      120     80           1      False
# 2     50   45              Vileplume  Grass  Poison   75      80       85      110       90     50           1      False
# 3     77   71             Victreebel  Grass  Poison   80     105       65      100       70     70           1      False
# 4    652  591              Amoonguss  Grass  Poison  114      85       70       85       80     30           5      False


# ******************************************************************************************************









