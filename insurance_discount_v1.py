# Import necessary libraries
import numpy as np
import pandas as pd

from DataAccessor import DataAccessor

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

# Generate sample data (replace this with your actual dataset)
path = 'data/smartwatch.csv'

# The DataAccessor accesses the csv file, cleans the data and return Numpy array
num_samples = 100
heart_data = DataAccessor().get_heart_data(path)
step_counts = DataAccessor().get_steps_data(path)
sleep_duration = DataAccessor().get_sleep_duration(path)


fitness_score = 0.5 * heart_data + 0.3 * step_counts + 0.2 * sleep_duration + np.random.normal(0, 5, num_samples)
fitness_level = ["low" if score < 100 else "moderate" if score < 200 else "high" for score in fitness_score]

# Combine features into a feature matrix
X = np.column_stack((heart_data, step_counts, sleep_duration))

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, fitness_score, test_size=0.2, random_state=42)
X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X, fitness_level, test_size=0.2, random_state=42)

# Linear Regression for Fitness Score Prediction
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict fitness scores
y_pred = lr_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (Fitness Score Prediction): {mse}")

# Classify Fitness Levels
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_cls, y_train_cls)

y_pred_cls = rf_classifier.predict(X_test_cls)
column = ['Health Level']

df = pd.DataFrame(y_pred_cls, columns=column)
print(df)
accuracy = accuracy_score(y_test_cls, y_pred_cls)
print(f"Accuracy (Fitness Level Classification): {accuracy}")
