df = pd.read_csv("patients.csv")

df['blood_pressure'].fillna(df['blood_pressure'].mean(), inplace=True)
df['heart_rate'].fillna(df['heart_rate'].mean(), inplace=True)

df['height'] = df['height'] / 100  # cm to meters

df['gender'] = df['gender'].str.title().replace({'M': 'Male', 'F': 'Female'})

df.drop(columns=['patient_id'], inplace=True)

print(df.head())
