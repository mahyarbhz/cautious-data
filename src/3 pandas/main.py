import pandas as pd

# ser = pd.Series({'a': 1, 2: 'b'})
# print(ser['a'], ser[2])
#
# print(pd.Series({'a': 1, 2: 'b'})['a'])
#
# print(ser.loc['a'])

# presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='age')
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

# print(presidents_df.iloc[15])
# print(presidents_df.iloc[15:18]) # get a range of data

# head(n=x) to access the first x rows
print(presidents_df[['age', 'height']])
