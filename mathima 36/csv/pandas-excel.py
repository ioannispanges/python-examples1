import pandas as pd

excel_data = pd.read_excel('student.xlsx', sheet_name='student')

print("Excel Data:")
print(excel_data.head())
