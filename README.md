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

# Lesson 12

```python
# SelectPercentile SelectKBest from sklearn can be used to select the most relevant features
# They follow the traditional fit/predict model
```

# Lesson 13 PCA

The faces example is in sklearn

# Lesson 14 Validation

Note that train_test_split is in model_selection in newer APIs and cross_validation in older version

Always fit on training data

transform and predict should use test data for validation, but DO NOT re-fit

[Cross validation](https://classroom.udacity.com/courses/ud120/lessons/2960698751/concepts/29483488390923):

[Problems](https://classroom.udacity.com/courses/ud120/lessons/2960698751/concepts/29483488390923) with splitting data into test and training set:
* Splitting the data forces you to have smaller data sets (anything in one set shrinks the other)
* [K-Fold Validation](https://classroom.udacity.com/courses/ud120/lessons/2960698751/concepts/29483488390923):
  1. Create K folds
  1. Each fold has 1 test set and K - 1 training sets
  1. Combine each training set grouping
  1. You now have K different test-train sets
  1. Do K trainings and average the results of each

## Nano notes
* ML is teaching computers to learn from past experiences