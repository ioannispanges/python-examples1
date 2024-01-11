import pandas as pd

data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

ages = pd.Series([25, 30, 22], name='Age')

print("DataFrame:")
print(df)
print("\nSeries:")
print(ages)
