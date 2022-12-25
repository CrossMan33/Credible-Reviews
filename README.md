# Credible-Reviews
Immutable reviews on the blockchain
This code uses the KMeans clustering algorithm from the scikit-learn library to create a model that will divide the data into two clusters.
The StandardScaler function is used to standardize the data, which helps to ensure that all input parameters are on the same scale and are weighted equally in the model.
The model is then fit to the data using the fit method, and the cluster labels for each data point are predicted using the predict method.

To assign weights to the clusters for paid reviewers between 0 and 1, based on the distance of each address to the center of the cluster, the following steps are taken:

Compute the cluster centers: First, the cluster centers are computed for the KMeans model. 
This is done by by calling the cluster_centers_ attribute of the model.

Compute the distances between the addresses and the cluster centers: 
Next, the distances between the addresses and the cluster centers are computed. This is done using the Euclidean distance formula.

Compute the weights: 
Finally, the weights for each address are computed by scaling the distances between 0 and 1.
where distance is the distance between the address and the cluster center, and max_distance is the maximum distance between any address and its cluster center.

Conclusion: 
This code loads the data, fits the KMeans model to the data, computes the cluster centers using the cluster_centers_ attribute, 
and then computes the distances between each address and its corresponding cluster center. 
Finally, it computes the weights for each address by scaling the distances between 0 and 1.
