from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from cnvrg import Experiment
import pickle

# Load the iris dataset
iris = load_iris()

# Define the features and target variable
X = iris.data
y = iris.target

# Train a decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Save the model as a pickle file
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)
    
# Log the precision of the model as a tag
precision = clf.score(X, y)
print(f"cnvrg_tag_precision: {precision}")


# Create a line chart with a custom name and value

e = Experiment()
e.log_param("precision", precision)
e.log_param("cnvrg_linechart_mychart", precision)
e.log_metric("precision", precision )
e.log_metric("Accuracy", Ys=[0.8, 0.9, 0.95])