from sklearn.datasets import load_iris
import pandas as pd

# 1. fortosi dataset irs
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

# 2. emfanisi stoixeiw
print("Iris Dataset Overview:")
print(iris_df.head())

# 3. ta dedomena gia ekpaideisi kai testarisma
from sklearn.model_selection import train_test_split

# X kai y metablites ekpaideusews
X = iris.data
y = iris.target

# to sunolo dedomenw kata 80% kai to allo to 20 % paei gia ekpaideusi training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Epilogi algorithou gia taksinomisi (Decision Tree)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# kathorismos tou Decision Tree

clf = DecisionTreeClassifier(random_state=42)

#  ekpaideuoume ton classifier sta dedomena mas

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("\nDecision Tree Classifier Results:")
print(f"Accurancy:{accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report")
print(class_report)
