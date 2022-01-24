import pandas as pd
df = pd.DataFrame({
    'sp' : ['MM1', 'MM1', 'MM1', 'MM2', 'MM2', 'MM2', 'MM4', 'MM4', 'MM4'],
    'mt' : ['S1', 'S1', 'S3', 'S3', 'S4', 'S4', 'S2', 'S2', 'S2'],
    'val' : ['a', 'n', 'cb', 'mk', 'bg', 'dgb', 'rd', 'cb', 'uyi'],
    'count' : [3,2,5,8,10,1,2,2,7]
    })

print(df)

df_grouped = df.groupby(['sp', 'mt']).agg({'count':'max'})
print(df_grouped)
df_grouped = df_grouped.reset_index()
print(df_grouped)
df_grouped = df_grouped.rename(columns={'count':'count_max'})

df = pd.merge(df, df_grouped, how='left', on=['sp', 'mt'])
print(df)
df = df[df['count'] == df['count_max']]
print(df)