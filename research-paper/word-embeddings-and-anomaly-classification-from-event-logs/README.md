---
description: 'WEAC : Word-Embeddings & Anomaly Classification from Event Logs'
---

# Word-Embeddings & Anomaly Classification from Event Logs

## Section 1 Highlights

### Word Embeddings

* **Definition**: A technique in Natural Language Processing (NLP) to represent words in a continuous vector space, capturing **semantic** and **syntactic** information.

#### Key Components

* **Semantic Information**: Focuses on the meaning or sense of words, their relationships, and context.
* **Syntactic Information**: Relates to the grammatical structure of sentences and the arrangement of words.

### Word2Vec

* **Definition**: A specific technique within word embeddings for representing words as vectors in a continuous vector space.
  * Techniques: **Skip-Gram** and **Continuous Bag of Words (CBOW)**.
  * **Comparison**: Word embedding is a broader concept, while Word2Vec is a more specialized and trained method.

#### Skip-Gram

* **Purpose**: Predict context words (surrounding words) given a target word.
* **How It Works**:
  * **Input**: A target word.
  * **Output**: Probabilities of the words in its context window.
  * **Objective**: Maximizes the probability of surrounding words appearing together with the target word.

#### Continuous Bag of Words (CBOW)

* **Purpose**: Predict the target word given its context (surrounding words).
* **How It Works**:
  * **Input**: All context words within the window.
  * **Output**: A single target word.
  * **Objective**: Maximizes the probability of the target word appearing in the context.

### Anomaly Classification Focus

* **Problem with Existing Algorithms**: They can detect anomalies but fail to identify the root cause.
* **Focus of This Work**: Anomaly classification, specifically identifying anomalous fields in event logs.

### The WEAC Model

* **Features**:
  * Detects anomalies and identifies anomalous features in event logs using word embeddings.
  * Treats event log features as "words" and their context as "neighboring features."
  * Provides **field-specific anomaly detection**, avoiding flagging the entire log.
* **Example**: A point-of-sale device accessing Dropbox is flagged as an anomaly, contrasting with regular network activities like guest mobile browsing Dropbox.

***

## Section 2 Highlights

### Existing Approaches

#### Event Log Mapping

* **Definition**: Converting text or categorical data into numerical vectors for machine learning analysis.
* **Techniques**:
  * **Word Embeddings**: Dense vectors capturing semantic and syntactic relationships.
  * **One-Hot Encoding**: Sparse binary vectors representing independent words or categories.

#### Word Embeddings vs. One-Hot Encoding

* **One-Hot Encoding**:
  * Words/features are independent and unrelated.
  * Creates sparse, high-dimensional binary vectors.
  * No semantic relationship captured.
  * **Example**:
    * Words: \["cat", "dog", "bird"]
    * Representations:
      * "cat" → \[1, 0, 0]
      * "dog" → \[0, 1, 0]
      * "bird" → \[0, 0, 1]
    * **Observation**: No indication that "cat" and "dog" are semantically similar.
* **Word Embeddings**:
  * Dense, continuous vectors (e.g., 300 dimensions vs. 10,000 in one-hot encoding).
  * Captures semantic and syntactic relationships.
  * **Example**:
    * Words: \["cat", "dog", "bird"]
    * Representations (hypothetical):
      * "cat" → \[0.8, 0.3, 0.2]
      * "dog" → \[0.79, 0.28, 0.21]
      * "bird" → \[0.1, 0.5, 0.9]
    * **Observation**: "Cat" and "dog" have similar vectors due to their shared semantic context.

### Techniques for Anomaly Detection

#### HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)

* **Definition**: An advanced clustering algorithm for identifying clusters and differentiating noise points.
* **Features**:
  * Extension of the DBSCAN algorithm.
  * Introduces hierarchical clustering.
  * Better handles varying density clusters.
* **Use Case**: Groups data points based on patterns or similarity.

#### Isolation Forests

* **Definition**: An unsupervised machine learning technique designed to isolate anomalies efficiently.
* **Features**:
  * Uses a tree-based approach.
  * Identifies anomalies by partitioning data recursively.
