**Workflow Pipeline**
<br>
By using these two scripts together, a workflow pipeline can be created where the first script trains and saves the model, 
and the second script loads and uses the trained model for predictions on new data.


**Task-1**<br>
This script loads the iris dataset using scikit-learn's `load_iris` function. 
It then defines the features as `X` and the target variable as `y`. 
Next, a decision tree classifier is trained on the data using `DecisionTreeClassifier` from scikit-learn. 
The model is saved as a pickle file named `model.pkl`. The precision of the model is logged as a tag using `clf.score` method. 
Finally, a line chart is created and logged to the cnvrg platform using `Experiment` class.

**Task-2**<br>
This script loads the iris dataset using scikit-learn's `load_iris` function. 
It then loads the saved model from the pickle file `model.pkl` located in `/input/train/` directory. 
The trained model is then used to predict class labels for new data, which is defined as a list of lists `X_new`. 
The predicted class labels are printed to the console using the `clf.predict` method.


By using these two scripts together, a workflow pipeline can be created where the first script trains and saves the model, 
and the second script loads and uses the trained model for predictions on new data.
