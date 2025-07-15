# import necessary libraries
import pandas as pd
import numpy as np

# set random seed, any number is fine but it's not true random
np.random.seed(42)

#1
dates = pd.date_range(start = '2023-01-01', end='2023-12-31', freq = 'D')
n = len(dates)

# Simulate sales data
data = pd.DataFrame({
    'date':dates,
    'region':np.random.choice(['North', 'South','East', 'West'], n),
    'customer_type': np.random.choice(['New', 'Returning'], n),
    'units_sold': np.random.poisson(lam = 20, size=n),
    'price_per_unit': np.random.normal(loc=50, scale=5, size=n)
})

# Simulate a drop in Q4 (Oct-Dec)
q4_mask = data['date'].dt.month >= 10
data.loc[q4_mask, 'units_sold'] = data.loc[q4_mask, 'units_sold'] * np.random.uniform(0.4, 0.7, size=q4_mask.sum())
data['units_sold'] = data['units_sold'].astype(int)

# Calculate total revenue
data['revenue'] = data['units_sold'] * data['price_per_unit']

# Save to CSV
import os
# Define the folder path
folder_path = "./data"

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

csv_path = os.path.join(folder_path, "prodct_sales_2023.csv")
data.to_csv(csv_path, index=False)

csv_path