import pandas as pd

ser = pd.Series({'a': 1, 2: 'b'})
print(ser['a'], ser[2])

print(pd.Series({'a': 1, 2: 'b'})['a'])

print(ser.loc['a'])
