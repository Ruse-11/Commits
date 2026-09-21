import pandas as pd
import matplotlib.pyplot as plt

# Data for 2 years
months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec'] * 2

years = ['2024']*12 + ['2025']*12

sales = [45000,52000,48000,61000,55000,67000,
         72000,69000,58000,63000,71000,78000,
         48000,55000,52000,65000,60000,73000,
         78000,75000,64000,70000,77000,85000]

# Create DataFrame
df = pd.DataFrame({'Year': years, 'Month': months, 'Sales': sales})

print("DATA:")
print(df)

# ---------------- ANALYSIS ----------------

# Year-wise total
year_total = df.groupby('Year')['Sales'].sum()
print("\nYear-wise Sales:")
print(year_total)

# Growth %
growth = ((year_total['2025'] - year_total['2024']) / year_total['2024']) * 100
print("\nYearly Growth (%):", growth)

# Monthly growth
df['MoM'] = df['Sales'].pct_change() * 100
print("\nMonth-wise Growth:")
print(df[['Month','MoM']].tail())

# ---------------- VISUALIZATION ----------------

# 1. Year-wise comparison
year_total.plot(kind='bar')
plt.title("Year-wise Sales")
plt.ylabel("Sales")
plt.show()

# 2. Sales Trend
plt.plot(df['Sales'], marker='o')
plt.title("Sales Trend (2 Years)")
plt.show()

# 3. Monthly Average (Seasonality)
monthly_avg = df.groupby('Month')['Sales'].mean()
monthly_avg.plot(kind='bar')
plt.title("Average Sales per Month")
plt.show()

# 4. Growth Graph
plt.plot(df['MoM'], marker='o')
plt.axhline(0)
plt.title("Month-over-Month Growth")
plt.show()