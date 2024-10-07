# Applying Principal Component Analysis (PCA) using scikit-learn

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd

# Load the iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

# Apply PCA to reduce dimensions (2 components)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualize the first two principal components
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target, cmap='plasma')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA - Iris Dataset')
plt.show()
