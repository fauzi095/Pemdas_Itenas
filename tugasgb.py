import pandas as pd

data = {'Nama': ['Jhon', 'Jane', 'Bob', 'Aice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

for index, x in df.iterrows():
    df.at[index, 'naik 5%'] = x['Gaji'] * 1.05

for index, x in df.iterrows():
    penaikan_umur = x['Gaji'] * 1.05 + (x['Gaji'] * 0.02) if x['Usia'] > 30 else x['Gaji'] * 1.05
    df.at[index, 'naik 2% (30 tahun)'] = penaikan_umur

print(df)
