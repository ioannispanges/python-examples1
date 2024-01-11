import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_data = pd.read_csv(url)

print("Head of the Titanic dataset:")
print(titanic_data.head())

print("\nInformation about the Titanic dataset:")
print(titanic_data.info())

print("\nDescriptive statistics of numeric columns:")
print(titanic_data.describe())

print("\nMissing values in Titanic dataset:")
print(titanic_data.isnull().sum())
