# HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)

HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) is an advanced clustering algorithm designed to identify clusters in data and differentiate noise points. It is an extension of the popular DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm, improving upon it by introducing hierarchical clustering and better handling of varying density clusters.

#### Key Features:

1. **Hierarchical Clustering:**
   * HDBSCAN builds a hierarchy of clusters based on density.
   * Unlike DBSCAN, which requires a single fixed `epsilon` (neighborhood size), HDBSCAN examines clusters at multiple levels of density.
2. **Varying Density Handling:**
   * It can detect clusters of different densities more effectively than DBSCAN.
   * This makes it more suitable for datasets where cluster densities are not uniform.
3. **Noise Identification:**
   * Like DBSCAN, it identifies noise points (outliers) as points that do not belong to any cluster.
4. **Minimal Parameters:**
   * The main parameter is `min_samples`, which controls the minimum number of points required to form a dense region.
   * There is no need to specify an `epsilon` value, as the algorithm automatically adapts to the data.
5. **Cluster Stability:**
   * HDBSCAN ranks clusters by their stability, allowing users to identify the most meaningful clusters.

#### Advantages:

* Works well with non-spherical and arbitrarily shaped clusters.
* Can handle large datasets efficiently.
* Identifies outliers naturally as part of the clustering process.
* Reduces reliance on tuning parameters like `epsilon`.

#### Applications:

* Anomaly detection
* Image segmentation
* Geospatial data analysis
* Customer segmentation
* Social network analysis

***

## Working

#### **1. Calculate Distances Between Points**

* Start by measuring the distance between each pair of points in the dataset (e.g., Euclidean distance).
* Use these distances to identify how close or far points are from each other.

#### **2. Compute Mutual Reachability Distance**

* Adjust the distances to account for density:
  * For each point, calculate its "core distance," which is the distance to its nearest neighbors (based on a parameter `min_samples`).
  * The **mutual reachability distance** between two points is the maximum of their core distances or their actual distance.
  * This ensures clusters can form even in areas of varying density.

#### **3. Build a Minimum Spanning Tree**

* Use the mutual reachability distances to create a **minimum spanning tree (MST)**.
* The MST is a graph that connects all points with the shortest total distance without forming loops.

#### **4. Build a Hierarchy of Clusters**

* Use the MST to create a **hierarchical tree**:
  * Start with all points as a single cluster.
  * Gradually remove the weakest connections (largest distances) in the tree, splitting the clusters into smaller groups.

#### **5. Select the Most Stable Clusters**

* Flatten the hierarchical tree to select meaningful clusters:
  * For each potential cluster, calculate its **stability**, which measures how long it persists in the hierarchy.
  * Keep the clusters with the highest stability and mark the remaining points as noise or outliers.

#### **6. Assign Labels to Points**

* Points in stable clusters are assigned cluster labels.
* Points not in any cluster are labeled as noise (`-1`).

***

#### **Key Parameters:**

* **`min_samples`**: Minimum number of points needed for a region to be considered dense.
* **`min_cluster_size`**: Minimum number of points required to form a cluster.

***

#### **Simple Analogy**

Imagine dropping marbles on a rubber sheet:

1. The marbles create dents in the sheet (dense areas).
2. The dents merge to form clusters as they sink deeper.
3. Shallow dents (outliers) are ignored as noise.

***

#### **Summary Steps:**

1. Calculate mutual reachability distances.
2. Build a minimum spanning tree of the data.
3. Create a hierarchy by progressively splitting clusters.
4. Extract the most stable clusters.
5. Label points as part of a cluster or as noise.

This process makes HDBSCAN highly effective at identifying clusters with varying densities and shapes, while also handling noise naturally.

***

#### Python Implementation:

HDBSCAN is implemented in Python and is available as a library: `hdbscan`. Below is an example of how to use it:

```python
pythonCopy codeimport hdbscan
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = np.random.rand(100, 2)

# Fit HDBSCAN
clusterer = hdbscan.HDBSCAN(min_samples=10, min_cluster_size=5)
cluster_labels = clusterer.fit_predict(data)

# Visualize results
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels, cmap='viridis', s=50)
plt.show()
```

This code clusters random data and visualizes the results, showing clusters with different colors and noise as a separate label.

***
