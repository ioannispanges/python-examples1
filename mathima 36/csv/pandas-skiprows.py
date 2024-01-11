import pandas as pd

skip_rows_data = pd.read_csv('student.csv', skiprows=2)

print("\nSkip Rows Data:")
print(skip_rows_data.head())
