
import pandas as pd
import numpy as np

# df = pd.read_csv('modified.csv')

# chunksize= # of rows
for df in pd.read_csv('modified.csv', chunksize=5):
    print("Chunk DF")
    print(df)


# ******************************************************************************************************************************************

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    res = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, res])

















