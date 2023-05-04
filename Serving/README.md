**Linear Regression Model for Housing Price Prediction**<br>

This script trains a linear regression model on the housing dataset to `predict` the price of a house based on the number of bedrooms, bathrooms, and square footage of living space. The script also defines a predict function that takes in the house features as a dictionary and returns the predicted price.

**Dependencies****<br>
- pandas <br>
- sklearn

**Usage**<br>

Load the housing dataset from the `/cnvrg/housing.csv` file.
Split the dataset into training and testing sets using the `train_test_split` function from `sklearn.model_selection`.
Train a linear regression model on the training data using the `LinearRegression` class from `sklearn.linear_model`.
Define a `predict` function that takes in the house features as a dictionary and returns the predicted price.
Call the `predict` function with the house features to get the predicted price.


curl -X POST \
    http://sa-endpoint1-2-1.aks-cicd-17945.cicd.cnvrg.me/api/v1/endpoints/yarwbqpneyosvxjzoffe \
-H 'Cnvrg-Api-Key: ZAJpQrDpK2iRC3PNi8uzrGtA' \
-H 'Content-Type: application/json' \
-d '{"input_params": {"bedrooms": 2, "bathrooms": 2, "sqft_living": 1200}}'
{"prediction":273062.91022360907}
