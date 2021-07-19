import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

n_samples = 300
random_state = 170

X, y = make_blobs(n_samples=n_samples, cluster_std=3.0, shuffle=False, random_state=random_state)
plt.scatter(X[:, 0], X[:, 1])
plt.show()
# Run k-means
kmeans = KMeans(n_clusters=3, init='random', max_iter=30, n_init=1, algorithm='full').fit(X)
y_pred = kmeans.predict(X)
X2, y2 = make_blobs(n_samples=n_samples, cluster_std=1.5, shuffle=False, random_state=random_state)
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
X_aniso = np.dot(X2, transformation)
X_varied, y_varied = make_blobs(n_samples=n_samples,cluster_std=[1.0, 2.5, 0.5],
random_state=random_state, shuffle=False)
X_filtered = np.vstack((X2[:100], X2[101:131], X2[201:215]))

