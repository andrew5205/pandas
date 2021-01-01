

# pd.DataFrame()


# pd.read_csv()
# pd.read_excel()


# df.head() - return first n rows - default 5 lines 
# df.tail() - return the last n rows - default 5 lines 



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
# print(df_txt)
# print(df_txt.head(5))
# print(df_txt.head(5))





