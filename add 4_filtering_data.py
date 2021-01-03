
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










# df.loc[] - Access a group of rows and columns by label(s) or a boolean array.
# column.str.contains('')

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
# Advance filtering 
contain_Mega = df.loc[df['Name'].str.contains('Mega')]
print(contain_Mega)
#        #                       Name    Type 1    Type 2   HP  ...  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 3      3      VenusaurMega Venusaur     Grass    Poison   80  ...      122      120     80           1      False
# 7      6  CharizardMega Charizard X      Fire    Dragon   78  ...      130       85    100           1      False
# 8      6  CharizardMega Charizard Y      Fire    Flying   78  ...      159      115    100           1      False
# 12     9    BlastoiseMega Blastoise     Water       NaN   79  ...      135      115     78           1      False
# ..   ...                  ...      ...     ...  ...     ...      ...      ...      ...    ...         ...        ...
# 591  531          AudinoMega Audino    Normal     Fairy  103  ...       80      126     50           5      False
# 796  719        DiancieMega Diancie      Rock     Fairy   50  ...      160      110    110           6       True


# ******************************************************************************************************
# ~ indicates NOT in pandas python 
not_Mega = df.loc[~df['Name'].str.contains('Mega')]
print(not_Mega)
#        #                 Name   Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0      1            Bulbasaur    Grass  Poison   45      49       49       65       65     45           1      False
# 1      2              Ivysaur    Grass  Poison   60      62       63       80       80     60           1      False
# 2      3             Venusaur    Grass  Poison   80      82       83      100      100     80           1      False
# 4      4           Charmander     Fire     NaN   39      52       43       60       50     65           1      False
# 5      5           Charmeleon     Fire     NaN   58      64       58       80       65     80           1      False
# ..   ...                  ...      ...     ...  ...     ...      ...      ...      ...    ...         ...        ...
# 794  718     Zygarde50% Forme   Dragon  Ground  108     100      121       81       95     95           6       True
# 795  719              Diancie     Rock   Fairy   50     100      150      100      150     50           6       True
# 797  720  HoopaHoopa Confined  Psychic   Ghost   80     110       60      150      130     70           6       True
# 798  720   HoopaHoopa Unbound  Psychic    Dark   80     160       60      170      130     80           6       True
# 799  721            Volcanion     Fire   Water   80     110      120      130       90     70           6       True

# [751 rows x 12 columns]



# ******************************************************************************************************

import re 
re_filter = df.loc[df['Type 1'].str.contains('Fire|Grass')]
print(re_filter)
#       #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0      1              Bulbasaur  Grass  Poison   45      49       49       65       65     45           1      False
# 1      2                Ivysaur  Grass  Poison   60      62       63       80       80     60           1      False
# 2      3               Venusaur  Grass  Poison   80      82       83      100      100     80           1      False
# 3      3  VenusaurMega Venusaur  Grass  Poison   80     100      123      122      120     80           1      False
# 4      4             Charmander   Fire     NaN   39      52       43       60       50     65           1      False
# ..   ...                    ...    ...     ...  ...     ...      ...      ...      ...    ...         ...        ...
# 735  667                 Litleo   Fire  Normal   62      50       58       73       54     72           6      False
# 736  668                 Pyroar   Fire  Normal   86      68       72      109       66    106           6      False
# 740  672                 Skiddo  Grass     NaN   66      65       48       62       57     52           6      False
# 741  673                 Gogoat  Grass     NaN  123     100       62       97       81     68           6      False
# 799  721              Volcanion   Fire   Water   80     110      120      130       90     70           6       True

# [122 rows x 12 columns]



pi_names = df.loc[df['Name'].str.contains('Pi[a-zA-Z]*')]
print(pi_names)
#        #        #                     Name    Type 1    Type 2   HP  ...  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 20    16                   Pidgey    Normal    Flying   40  ...       35       35     56           1      False
# 21    17                Pidgeotto    Normal    Flying   63  ...       50       50     71           1      False
# 22    18                  Pidgeot    Normal    Flying   83  ...       70       70    101           1      False
# 23    18      PidgeotMega Pidgeot    Normal    Flying   83  ...      135       80    121           1      False
# 30    25                  Pikachu  Electric       NaN   35  ...       50       50     90           1      False
# 136  127                   Pinsir       Bug       NaN   65  ...       55       70     85           1      False
# 137  127        PinsirMega Pinsir       Bug    Flying   65  ...       65       90    105           1      False
# 186  172                    Pichu  Electric       NaN   20  ...       35       35     60           2      False
# 219  204                   Pineco       Bug       NaN   50  ...       35       35     15           2      False
# 239  221                Piloswine       Ice    Ground  100  ...       60       60     50           2      False
# 438  393                   Piplup     Water       NaN   53  ...       61       56     40           4      False
# 558  499                  Pignite      Fire  Fighting   90  ...       70       55     55           5      False
# 578  519                   Pidove    Normal    Flying   50  ...       36       30     43           5      False
# 716  648  MeloettaPirouette Forme    Normal  Fighting  100  ...       77       77    128           5      False

# [14 rows x 12 columns]







