#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import math
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import scipy.stats

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
# classifier = DecisionTreeClassifier(random_state=0, min_samples_split=2)
# classifier.fit(features_train, labels_train)
# predictions = classifier.predict(features_test)
# print(accuracy_score(labels_test, predictions))

classifier = DecisionTreeClassifier(random_state=0, min_samples_split=40)
classifier.fit(features_train, labels_train)
predictions = classifier.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)
#########################################################

num_features = len(features_train[0])

#print scipy.stats.entropy([2,1], base=2)


