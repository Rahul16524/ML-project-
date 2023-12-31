# -*- coding: utf-8 -*-
"""decision tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aJ3J0nsXx2wtH20WpOCfapmlUpTsnGKk
"""

!pip install -U scikit-learn
import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

from google.colab import files
uploaded = files.upload()

import io
import pandas as pd
import graphviz
from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
df2 = pd.read_csv(io.BytesIO(uploaded['Salary-Data.csv']))

# Split the data into training and testing sets
test_size = float(input("Enter test data size (between 0 and 1): "))
train_data = df2.sample(frac=1-test_size, random_state=42)
test_data = df2.drop(train_data.index)

# Extract the features and target variable
X_train = train_data['YearsExperience'].values.reshape(-1, 1)
y_train = train_data['Salary'].values.reshape(-1, 1)
X_test = test_data['YearsExperience'].values.reshape(-1, 1)
y_test = test_data['Salary'].values.reshape(-1, 1)

# Train the decision tree model
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

# Make predictions on the test data
y_pred = dt.predict(X_test)

# Calculate the mean squared error and coefficient of determination (R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Accuracy score: {:.2f}".format(r2))

# Export the decision tree as a DOT file
dot_data = export_graphviz(dt, out_file=None, feature_names=['Years of Experience'])

# Generate a graph from the DOT file
graph = graphviz.Source(dot_data, format='png')

# Save the graph as a PNG file
graph.render('decision_tree')

# Display the graph
graph

# # Download the graph as a PNG file
# from google.colab import files
# files.download('decision_tree.png')