import pandas as pd
import matplotlib as plt
df = pd.read_csv('./pandas/reader.csv')
total_weight = df.weight.sum()
print(total_weight)
obese = df.weight > 70
print(obese)
print(df[obese])
new_sorted= df.sort_values('weight',ascending=True)
print(new_sorted)
height_w=df[['weight','height']].sum()
print(height_w)
dat = pd.to_datetime(df.bday)
df['month']=pd.DatetimeIndex(df.bday).month
df['year']=pd.DatetimeIndex(df.bday).year
df['day']=pd.DatetimeIndex(df.bday).day
df['weekday']=pd.DatetimeIndex(df.bday).weekday
print(df.groupby('weekday')[['weight']].mean())
# print(df)
df.weight.plot()