import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
        'Age': [25, 30, 25, 22, 30],
        'Occupation': ['Engineer', 'Data Scientist', 'Engineer', 'Student', 'Data Scientist']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_renamed = df.rename(columns={'Name': 'Full Name', 'Age': 'Years'})

print("\nDataframe renamed:")
print(df_renamed)
