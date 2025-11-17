import pandas as pd

df = pd.read_csv("employees.csv")   # load your employee data

# Handle missing values
df['salary'].fillna(df['salary'].mean(), inplace=True)
df['department'].fillna("Unknown", inplace=True)
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')

# Standardize department names
df['department'] = df['department'].str.upper().replace({'HUMAN RESOURCES': 'HR'})

# Encode categorical columns
df = pd.get_dummies(df, columns=['department', 'job_role'])

print(df.head())
