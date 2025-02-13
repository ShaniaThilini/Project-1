import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "car_prices.csv"
df = pd.read_csv(file_path)

# Ensure df and pd are properly initialized
if 'df' not in locals():
    df = pd.DataFrame()

# Drop duplicate rows if any
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Convert 'saledate' to datetime format with UTC to avoid warnings
df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce', utc=True)

# Convert 'condition' column to numeric if it's not already
if df['condition'].dtype == 'object':
    df['condition'] = pd.to_numeric(df['condition'], errors='coerce')

# Ensure 'odometer' and 'sellingprice' are numeric
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
df['sellingprice'] = pd.to_numeric(df['sellingprice'], errors='coerce')

# Remove any rows where key values are still missing after conversion
df = df.dropna(subset=['condition', 'odometer', 'sellingprice'])

# Scatter Plot: Mileage vs. Selling Price
plt.figure(figsize=(10, 6))
plt.scatter(df['odometer'], df['sellingprice'], alpha=0.5)
plt.xlabel("Mileage (Odometer Reading)")
plt.ylabel("Selling Price")
plt.title("Impact of Mileage on Selling Price")
plt.show()

# Display the cleaned dataset info
df.info()

# Line Graph: Average Selling Price by Condition (Rounded)
# Create the 'condition_rounded' column before filtering
df['condition_rounded'] = df['condition'].round(0)

# Filter out condition values outside a reasonable range (e.g., 1-10)
df_filtered = df[(df['condition_rounded'] >= 1) & (df['condition_rounded'] <= 10)]

# Group by condition and calculate average selling price
condition_avg_price = df_filtered.groupby('condition_rounded')['sellingprice'].mean()

plt.figure(figsize=(10, 6))
plt.plot(condition_avg_price.index, condition_avg_price.values, marker='o', linestyle='-')
plt.xlabel("Rounded Condition")
plt.ylabel("Average Selling Price")
plt.title("Corrected Average Selling Price by Condition")
plt.grid(True)
plt.show()

# Display the cleaned dataset info
df.info()