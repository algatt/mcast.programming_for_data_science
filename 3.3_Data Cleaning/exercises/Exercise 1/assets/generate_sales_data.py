import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(0)

# Generate a DataFrame
dates = pd.date_range(start="2021-01-01", end="2021-01-30")
data = {
    'Date': np.random.choice(dates, size=100),
    'Sales': np.random.randint(100, 500, size=100) * np.random.choice([1, np.nan], size=100, p=[0.9, 0.1]),
    'CustomerID': np.random.choice(range(1, 20), size=100),
    'Product': np.random.choice(['Product A', 'Product B', 'Product C', 'Product D'], size=100),
    'Quantity': np.random.randint(1, 10, size=100),
}

df = pd.DataFrame(data)

# Introduce duplicates
df = pd.concat([df, df.iloc[:5]], ignore_index=True)

# Introduce some outliers in 'Sales'
df.loc[95:99, 'Sales'] *= 10

# Save the DataFrame to a CSV file
# df.to_csv('sales_data.csv', index=False)
df[:90].to_csv('sales_data.csv', index=False)
df[90:].to_csv('sales_data_extra.csv', index=False)
