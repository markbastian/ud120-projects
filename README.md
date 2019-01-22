ud120-projects
==============

Starter project code for students taking Udacity ud120

## Notes

## Classifiers

* Naive Bayes
* SVM (SVC - C = Classifier)
* Decision Tree
  * Ensemble methods
    * Adaboost
    * Random Forest

# Lesson 6: Datasets and Questions
More Data > Fine Tuned Algorithm
Data Types
 * Numerical (discrete or continuous?)
 * Categories/Enums
 * Time series (date/time stamp)
 * text
 
# Lesson 7: Regressions + Continuous Supervised Learning
 * Continuous meaning a continuous output range, not continuously learning
 * Continuous vs. Discrete
 
 Result is often just a simple line fit (y = mx + b)
 
 reg.predict takes an array
 reg.coef_ & reg.intercept_
 reg.score provides r**2

Classification vs. Regression
Discrete vs. Continuous
Decision Boundary vs. Best Fit Line
Accuracy vs. Sum of Squares/R^2 to determine accuracy

# Lesson 8 : Outliers

# Lesson 9 : Unsupervised Learning
Data is unlabeled

 * Clustering
   * K-means is most common
 * Dimensionality Reduction
 
# Lesson 10
https://scikit-learn.org/stable/modules/preprocessing.html
https://scikit-learn.org/stable/modules/preprocessing.html#scaling-features-to-a-range

* Key is you need a numpy array
* Scaling only affects algorithms in which > 1 dimension are compared
  * Tip - if only horizontal and vertical lines split the data only one dimension is used so scaling doesn't matter
  
# Lesson 11 : Learning from text
Bag of Words - A frequency count of words 
Stop words (A, and, of,...) are often removed
Generally just word stems are used (e.g. love in loves)

```python
# stopwords
from nltk.corpus import stopwords
len(stopwords.words('english'))

# Stemming
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

# TF/IDF : Term frequency, inverse document frequency

```

