import pandas as pd
import matplotlib.pyplot as plt

# Monthly data
months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']

sales = [45000,52000,48000,61000,55000,67000,
         72000,69000,58000,63000,71000,78000]

# Create DataFrame
df = pd.DataFrame({'Month': months, 'Sales': sales})

# Display data
print("Monthly Sales Data:")
print(df)

# Calculations
total = df['Sales'].sum()
avg = df['Sales'].mean()

print("\nTotal Sales:", total)
print("Average Sales:", avg)

# Max and Min
print("\nHighest Sales Month:")
print(df.loc[df['Sales'].idxmax()])

print("\nLowest Sales Month:")
print(df.loc[df['Sales'].idxmin()])

# Above average
print("\nMonths Above Average:")
print(df[df['Sales'] > avg])

# ---------------- VISUALIZATION ----------------

# 1. Bar Chart
plt.figure()
plt.bar(df['Month'], df['Sales'])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 2. Line Graph
plt.figure()
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title("Sales Trend")
plt.show()

# 3. Above/Below Average
colors = ['green' if x > avg else 'red' for x in df['Sales']]
plt.figure()
plt.bar(df['Month'], df['Sales'], color=colors)
plt.axhline(avg)
plt.title("Above/Below Average")
plt.show()

# 4. Histogram
plt.figure()
plt.hist(df['Sales'])
plt.title("Sales Distribution")
plt.show()