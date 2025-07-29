import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

sns.set(style="whitegrid")

try:
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

    print("=== First 5 Rows ===")
    print(df.head())

    print("\n=== Data Types ===")
    print(df.dtypes)

    print("\n=== Missing Values ===")
    print(df.isnull().sum())

    df.dropna(inplace=True)

    print("\n=== Descriptive Statistics ===")
    print(df.describe())

    print("\n=== Grouped Means by Species ===")
    group_means = df.groupby('species').mean()
    print(group_means)

    plt.figure(figsize=(8, 4))
    plt.plot(df.index[:50], df['sepal length (cm)'][:50], label='Sepal Length')
    plt.title('Sepal Length Trend (first 50 samples)')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    sns.histplot(df['sepal width (cm)'], kde=True, bins=20, color='orange')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: Dataset file not found.")
except pd.errors.ParserError:
    print("Error: Could not parse the dataset.")
except Exception as e:
    print(f"Unexpected error: {e}")
