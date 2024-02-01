from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

newgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'), random_state=42)

X_train, X_test, y_train, y_test = train_test_split(newgroups.data, newgroups.target, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()

x_train_bow = vectorizer.fit_transform(X_train)
x_test_bow = vectorizer.transform(X_test)

nb_classifier = MultinomialNB()
nb_classifier.fit(x_train_bow, y_train)

predictions = nb_classifier.predict(x_test_bow)

accuracy = accuracy_score(y_test, predictions)

classification_rep = classification_report(y_test, predictions, target_names=newgroups.target_names)

print("20 Newsgroups Dataset:")
print("Number of Categories", len(newgroups.target_names))
print("\nModel Evaluation: ")
print("Accuracy: ", accuracy)
print("\nClassification Report:\n", classification_rep)
