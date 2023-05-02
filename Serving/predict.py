import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load the housing dataset
df = pd.read_csv('/cnvrg/housing.csv')

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['bedrooms', 'bathrooms', 'sqft_living']], df['price'], test_size=0.2, random_state=42)

# train a linear regression model on the training data
model = LinearRegression()
model.fit(X_train, y_train)

# define a predict function that takes in the house features and returns the predicted price
def predict(input_dict):
    try:
        bedrooms = input_dict['bedrooms']
        bathrooms = input_dict['bathrooms']
        sqft_living = input_dict['sqft_living']
        features = [[bedrooms, bathrooms, sqft_living]]
        prediction = model.predict(features)[0]
        message = f"The predicted price is {prediction}."
        print(message)
        return float(prediction)
    except:
        return "Error: could not make prediction."

# test the predict function on a sample input
#sample_input = {"bedrooms": 3, "bathrooms": 2, "sqft_living": 1500}
#predicted_price = predict(sample_input)
#print(predicted_price)
