# ======================================
# Assignment: Analyzing Data with Pandas 
# and Visualizing Results with Matplotlib
# ======================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --------------------------------------
# Task 1: Load and Explore the Dataset
# --------------------------------------

# Load Iris dataset from sklearn
iris = load_iris(as_frame=True)
df = iris.frame  # convert to pandas DataFrame
df['species'] = iris.target_names[iris.target]  # add species column

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Explore dataset structure
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# (No missing values in Iris, but here’s an example if cleaning is needed)
# df.fillna(df.mean(), inplace=True)  # fill missing numeric values

# --------------------------------------
# Task 2: Basic Data Analysis
# --------------------------------------

# Descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Grouping by species and computing mean
species_means = df.groupby("species").mean()
print("\nAverage measurements per species:")
print(species_means)

# Identify interesting pattern
print("\nObservation: Iris-setosa generally has smaller petal measurements compared to others.")

# --------------------------------------
# Task 3: Data Visualization
# --------------------------------------

# 1. Line chart - cumulative sum of sepal length (to simulate a trend)
plt.figure(figsize=(8,5))
df["sepal length (cm)"].cumsum().plot(kind="line")
plt.title("Cumulative Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Cumulative Sepal Length")
plt.show()

# 2. Bar chart - average petal length per species
species_means["petal length (cm)"].plot(kind="bar", color=["blue","orange","green"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.hist(df["sepal width (cm)"], bins=15, color="purple", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=df["target"], cmap="viridis")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()

# (Optional) Using seaborn for nicer style
sns.pairplot(df, hue="species")
plt.suptitle("Pairwise Relationships of Iris Features", y=1.02)
plt.show()

# --------------------------------------
# Error Handling Example
# --------------------------------------
try:
    missing_file = pd.read_csv("non_existent.csv")
except FileNotFoundError:
    print("\nError: File not found. Please check the file path!")
