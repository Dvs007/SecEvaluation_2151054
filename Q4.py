import pandas as pd
import matplotlib.pyplot as plt

# Load a sample sales dataset (replace with your data)
data = pd.read_csv("sales_data.csv")

# Analyze sales trends over time
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Create a sales chart
data['Total Sales'].plot(kind='line')
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

# Identify peak sales hours and popular products
peak_sales_hour = data['Hour'].value_counts().idxmax()
popular_product = data['Product'].value_counts().idxmax()

# Generate reports for store management
print(f"Peak Sales Hour: {peak_sales_hour}")
print(f"Most Popular Product: {popular_product}")
