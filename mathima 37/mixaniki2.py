import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

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

preprocessor = ColumnTransformer(
    transformers=[
        ('inputer', SimpleImputer(strategy='mean'), ['Age', 'Salary']),
        ('encoder', OneHotEncoder(), ["Gender"])
    ],
    remainder='passthrough'
)

pipeline = Pipeline(steps=[('preprocessor'), preprocessor])

x_tranformed = pipeline.fit_transform(df.drop('Label', axis=1))
y = df['Label']

preprocessed_df = pd.concat([pd.DataFrame(x_tranformed), y], axis=1)
print("\nPreprocessed Dataset:")
print(preprocessed_df)

X_train, X_Test, y_train, y_test = train_test_split(x_tranformed, test_size=0.2, random_state=42)

print("\nTraining Set:")
print(pd.DataFrame(X_train), y_train)
print("\nTesting Set:")
print(pd.DataFrame(X_Test), y_test)
