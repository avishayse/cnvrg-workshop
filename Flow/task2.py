import pickle
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the iris dataset
iris = load_iris()

# Load the saved model from the pickle file
#/input/<task_name>/model.pkl

with open('/input/train/model.pkl', 'rb') as f:
    clf = pickle.load(f)

# Use the trained model to make predictions on new data
X_new = [[5.0, 3.2, 1.2, 0.2], [6.0, 3.0, 4.8, 1.8], [6.9, 3.1, 5.4, 2.1]]
y_new = clf.predict(X_new)

# Print the predicted class labels for the new data
print(y_new)