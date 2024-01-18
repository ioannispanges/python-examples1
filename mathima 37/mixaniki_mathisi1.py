import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Creating a simple dataset with missing values
data = {
    'Age': [25, 30, np.nan, 22, 25],
    'Gender': ['Male', 'Female', 'Male', 'Female', np.nan],
    'Salary': [50000, 60000, 75000, np.nan, 80000],
    'Label': ['A', 'B', 'A', 'B', 'A']
}

df = pd.DataFrame(data)

print('Original Dataset:')
print(df)

# Imputing missing values in the 'Age' column with mean
imputer = SimpleImputer(strategy='mean')
df['Age'] = imputer.fit_transform(df[['Age']])

print("\nDataset after Imputation:")
print(df)

# One-Hot Encoding for categorical columns 'Gender' and 'Label'
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_categorical = pd.DataFrame(encoder.fit_transform(df[['Gender', 'Label']]))
df = pd.concat([df, encoded_categorical], axis=1)
df = df.drop(['Gender', 'Label'], axis=1)

print("\nDataset after One-Hot Encoding:")
print(df)
