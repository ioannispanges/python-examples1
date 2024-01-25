import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris_data = iris.data
iris_labels = iris.target
iris_feauture_names = iris.feature_names

iris_df = pd.DataFrame(data=iris_data, columns=iris_feauture_names)
iris_df['Species'] = iris_labels

sns.set(style="ticks")
sns.pairplot(iris_df, hue="Species", markers=["o", "s", "D"])
plt.show()
