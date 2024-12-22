# Word Embedding for Anomaly Detection

## What is word embedding?

Word Embedding is the <mark style="color:yellow;">**mathematical representation of words in continuous vector space**</mark>. \
\
In continuous vector space, words with similar meanings or contexts have similar vector representations. what this means is _<mark style="color:yellow;">rather than giving each word a unique binary identity we map similar words and their relationship with real numbers</mark>_, like giving words a vector position in space.\


### examples -

1. "dog": \[0.25, 0.64, -0.15, …] \
   "puppy": \[0.26, 0.65, -0.16, …]\
   \
   here there is a slight difference since these are close to each other but not same\

2. "hot": \[0.3, -0.5, 0.7, …] \
   "cold": \[-0.4, 0.6, -0.8, …]\
   \
   here in this example even though they are counter apart, but they are not geometrically opposite to each other, the reason being is their positioning depends on various references and context they are used in.\

3. king: \[0.6, 0.7, -0.2, …] \
   man: \[0.2, 0.5, 0.1, …] \
   woman: \[0.1, 0.6, -0.1, …]\
   \
   <mark style="color:red;">**queen = king − man + woman**</mark>\
   \
   queen: \[0.5,0.8,−0.4,…] \
   \
   here in this example, we established a relation among the various entities
