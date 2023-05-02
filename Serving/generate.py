import pandas as pd

# Create a DataFrame with the desired columns
data = {'bedrooms': [1, 2, 3, 4, 5, 2, 3, 4, 1, 2, 3, 4, 5, 3, 2, 1, 4, 3, 2, 5], 
        'bathrooms': [1, 1.5, 2, 2.5, 3, 2, 2.5, 3, 1, 1, 1.5, 2, 2.5, 2, 1.5, 1, 3, 2.5, 2, 3], 
        'sqft_living': [500, 1000, 1500, 2000, 2500, 1200, 1700, 2200, 800, 950, 1250, 1750, 2250, 1500, 900, 700, 2100, 1800, 1100, 2800], 
        'price': [100000, 200000, 300000, 400000, 500000, 250000, 350000, 450000, 150000, 175000, 225000, 275000, 325000, 275000, 185000, 135000, 475000, 400000, 250000, 600000]}

df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('housing.csv', index=False)
