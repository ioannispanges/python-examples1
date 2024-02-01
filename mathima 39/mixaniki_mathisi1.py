from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
x = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

svc_model = SVC(kernel='linear', C=1)
svc_model.fit(X_train, y_train)

prediction = svc_model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Iris Dataset:")
print("Number of samples: ", len(x))
print("Number of features: ", len(x[0]))
print("\nModel Evaluation: ")
print("Accuracy or Evaluation:", accuracy)
