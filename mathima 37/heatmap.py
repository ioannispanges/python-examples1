import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'flights' dataset
flights_data = sns.load_dataset("flights")

# Pivot the dataset
correlation_matrix = flights_data.pivot(index='month', columns='year', values='passengers')

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt='g')
plt.xlabel('Year')
plt.ylabel('Month')
plt.title('Heatmap Example')
plt.show()
