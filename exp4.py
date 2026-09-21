import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("="*60)
print("DIABETES DATA ANALYSIS")
print("="*60)

# Create dataset
np.random.seed(0)
data = {
    'Glucose': np.random.randint(80,180,50),
    'BMI': np.random.randint(18,35,50),
    'Age': np.random.randint(20,60,50)
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df.head())

# Statistics
print("\nStatistics:")
print(df.describe())

# Mean, variance
print("\nMean:")
print(df.mean())

print("\nVariance:")
print(df.var())

# ---------------- REGRESSION ----------------

X = df[['Glucose']]
y = df['BMI']

model = LinearRegression()
model.fit(X,y)

print("\nRegression Equation:")
print("BMI =", model.intercept_, "+", model.coef_[0], "* Glucose")

# ---------------- VISUALIZATION ----------------

# 1. Histogram
df.hist(figsize=(8,6))
plt.suptitle("Distribution")
plt.show()

# 2. Scatter
plt.scatter(df['Glucose'], df['BMI'])
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Glucose vs BMI")
plt.show()

# 3. Regression line
plt.scatter(df['Glucose'], df['BMI'])
plt.plot(df['Glucose'], model.predict(X))
plt.title("Regression Line")
plt.show()

# 4. Box plot
df.plot(kind='box')
plt.title("Box Plot")
plt.show()

print("\nAnalysis Completed")