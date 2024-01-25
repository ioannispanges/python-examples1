import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

np.random.seed(42)
num_samples = 100
num_bedrooms = np.random.randint(1, 6, size=num_samples)
house_prices = 50 * num_bedrooms + 30 + np.random.normal(scale=10, size=num_samples)

X_train, x_test, y_train, y_test = train_test_split(num_bedrooms.reshape(-1, 1), house_prices, test_size=0.2,
                                                    random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(x_test)

mse = mean_squared_error(y_test, predictions)

print("Sample Data:")
print("Number of bedrooms:", x_test.flatten()[:5])
print("Actual house prices:", y_test[:5])
print("Predicted house prices:", predictions[:5])
print("\nModel Evaluation")
print("Mean Squared Error:", mse)
