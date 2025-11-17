df = pd.read_csv("sales.csv")

df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['Month-Year'] = df['transaction_date'].dt.to_period('M')

df = df[df['transaction_amount'] > 0]   # remove invalid transactions

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['transaction_amount'] = scaler.fit_transform(df[['transaction_amount']])

print(df.head())
