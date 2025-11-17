import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("finance.csv")

df['stock_price'].fillna(df['stock_price'].mean(), inplace=True)
df['volume'].fillna(df['volume'].mean(), inplace=True)

df['MA_7'] = df['stock_price'].rolling(window=7).mean()
df['MA_30'] = df['stock_price'].rolling(window=30).mean()

scaler = StandardScaler()
df[['stock_price', 'volume']] = scaler.fit_transform(df[['stock_price', 'volume']])

df = pd.get_dummies(df, columns=['sector', 'company_name'])
print(df.head())
