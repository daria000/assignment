import pandas as pd

# Path to the Airbnb dataset
file_path = 'data/raw/airbnb/airbnb.csv'

# Load the Airbnb dataset
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit()


# Calculate mean, median, and count for the apartment price using loops
price_values = df['price'].dropna()  # Drop missing values if any

# Initialize variables
total_price = 0
count = 0

# Calculate total price and count
for price in price_values:
    total_price += price
    count += 1

# Calculate mean
mean_price = total_price / count

# Calculate median
sorted_prices = sorted(price_values)
mid = count // 2
median_price = (sorted_prices[mid] + sorted_prices[mid - 1]) / 2 if count % 2 == 0 else sorted_prices[mid]

# Print results
print(f"Mean price: ${mean_price:.2f}")
print(f"Median price: ${median_price:.2f}")
print(f"Count of prices: {count}")
