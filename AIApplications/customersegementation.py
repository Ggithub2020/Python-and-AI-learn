from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
# Sample customer data: [Annual Income, Spending Score]
data = [[15, 39], [16, 81], [17, 6], [18, 77], [19, 40], [20, 76], [21, 6]]
df = pd.DataFrame(data, columns=["Income", "SpendingScore"])

# KMeans Clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(df)

# Add labels
df['Cluster'] = kmeans.labels_

# Plot
plt.scatter(df['Income'], df['SpendingScore'], c=df['Cluster'], cmap='viridis')
plt.title("Customer Segments")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.grid(True)
plt.show()
