import pandas as pd


data = {
    'event': ['Launch', 'Update', 'Maintenance', 'Review'],
    'date': ['2023-01-15 14:30', '2023-03-22 09:00', '2023-06-10 23:45', '2023-09-05 08:15']
}
df = pd.DataFrame(data)
print(df)


df['date'] = pd.to_datetime(df['date'])


df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
df['quarter'] = df['date'].dt.quarter


print(df)