import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_excel('data/AI ML Internship Training Data.xlsx')

# Basic statistics
print(data.describe())

# Visualizations
plt.figure(figsize=(10, 6))
sns.countplot(x='Delayed', data=data)
plt.title('Distribution of Delay')
plt.show()

# Correlation heatmap
corr = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
