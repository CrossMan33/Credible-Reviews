import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the data and standardize the data
# data = np.loadtxt('data.csv', delimiter=',')
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[:,1:])

# Fit the model to the data
model = KMeans(n_clusters=2)
model.fit(scaled_data)

# Compute the cluster centers
cluster_centers = model.cluster_centers_

# Compute the distances between the addresses and the cluster centers
distances = []
for address in scaled_data:
    distance = np.sqrt(np.sum((address -cluster_centers[model.predict([address])[0]])**2))
    distances.append(distance)

# Compute the weights
max_distance = max(distances)
weights = [1 - distance / max_distance for distance in distances]

# Create a Pandas dataframe with the Ethereum addresses and their weights
df = pd.DataFrame({'Address': data[:,0], 'Weight': weights})

# Output the dataframe to a CSV file
df.to_csv('weights.csv', index=False)