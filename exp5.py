import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

print("="*60)
print("ADVANCED PLOTTING")
print("="*60)

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

print("\nDataset Shape:", df.shape)
print(df.head())

# ---------------- NORMAL CURVE ----------------
data = df['sepal length (cm)']
mean = data.mean()
std = data.std()

x = np.linspace(data.min(), data.max(), 100)

plt.hist(data, bins=20, density=True)
plt.plot(x, (1/(std*np.sqrt(2*np.pi))) * np.exp(-((x-mean)**2)/(2*std**2)))
plt.title("Normal Curve")
plt.show()

# ---------------- DENSITY PLOT ----------------
df['petal length (cm)'].plot(kind='kde')
plt.title("Density Plot")
plt.show()

# ---------------- SCATTER + CORRELATION ----------------
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'])
plt.title("Scatter Plot")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

sns.heatmap(df.iloc[:,:4].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# ---------------- HISTOGRAM ----------------
df.iloc[:,:4].hist(figsize=(8,6))
plt.suptitle("Histograms")
plt.show()

# ---------------- 3D PLOT ----------------
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2])
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")

plt.title("3D Scatter Plot")
plt.show()

print("\nAll plotting completed")