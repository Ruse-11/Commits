import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

print("="*60)
print("IRIS DATASET ANALYSIS")
print("="*60)

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({0:'setosa',1:'versicolor',2:'virginica'})

print("\nDataset Loaded Successfully")
print("Shape:", df.shape)

# Display data
print("\nFirst 10 Rows:")
print(df.head(10))

# Basic info
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Descriptive statistics
print("\nStatistics:")
print(df.describe())

# Group analysis
print("\nSpecies-wise Analysis:")
print(df.groupby('species_name').mean())

# Correlation
corr = df.iloc[:,:4].corr()
print("\nCorrelation Matrix:")
print(corr)

# Additional stats
for col in df.columns[:4]:
    print(f"\n{col}")
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Std Dev:", df[col].std())

# ---------------- VISUALIZATION ----------------

# 1. Histogram
df.iloc[:,:4].hist(figsize=(8,6))
plt.suptitle("Feature Distribution")
plt.show()

# 2. Box Plot
df.iloc[:,:4].plot(kind='box')
plt.title("Box Plot")
plt.show()

# 3. Scatter Plot
plt.scatter(df.iloc[:,0], df.iloc[:,1])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot")
plt.show()

# 4. Heatmap
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

print("\nAnalysis Completed")