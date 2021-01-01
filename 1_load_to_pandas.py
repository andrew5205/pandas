

# pd.DataFrame()


# pd.read_csv()
# pd.read_excel()


# df.head() - return first n rows - default 5 lines 
# df.tail() - return the last n rows - default 5 lines 
# df.columns() - return the column label of the data frame - pandas.core
# df.iloc() - integer-location based index
# df.iterrows() - Iterate over DataFrame rows as (index, Series) pairs.
# df.loc() - Access a group of rows and columns by label(s) or a boolean array.

# df.sort_index() - Sort object by labels (along an axis).
                    # (axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
# df.sort_values() - Sort by the values along either axis.
                    # (by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)[source])



# ******************************************************************************************************
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# print(df)
# print(df.head(5))
# print(df.tail(5))


df_exls = pd.read_excel('pokemon_data.xlsx')
# print(df_exls)
# print(df_exls.head(3))
# print(df_exls.tail(3))


df_txt = pd.read_csv('pokemon_data.txt', delimiter= '\t')
# print( df_txt)
# print(df_txt.head(5))
# print(df_txt.head(5))

# ******************************************************************************************************
# READ HEADER
print(df.columns)
# Index(['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk',
#         'Sp. Def', 'Speed', 'Generation', 'Legendary'],
#         dtype='object')


# Read each column
print(df['Name'])
print(df.Name)
print(df['Name'][:5])
print(df[['Name', 'Type 1', 'HP']])


# Read each row
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[:4])

for index, row in df.iterrows():
    print(index, row)
    # print(index, row['Name'])

# more like search specific tag
print(df.loc[df['Type 1'] == "Fire"])


# Read a specific location(R, C)
print(df.iloc[2, 1]) 

# sort_value
print(df.sort_values(['Type 1', 'HP'], ascending=False)
print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))

# ******************************************************************************************************

















