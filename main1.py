import pandas as pd

df = pd.read_csv('master.csv')

col = df.iloc[:, 6].values
nianfen = df.iloc[:, 1].values

sum = 0
last_year = nianfen[0]
last_i = 0
num_index = 0
for i, v in enumerate(col):
    num_index += 1
    sum += v
    if nianfen[i] != last_year or i == (len(col)-1):
        for j in range(last_i, i):
            df.iloc[j, 7] = sum/num_index
        last_i = i
        last_year = nianfen[i]
        num_index = 0
        sum = 0

df.to_csv('master1.csv')
print(df.iloc[:, 7].values)
