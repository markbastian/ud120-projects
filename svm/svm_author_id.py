#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
classifier = svm.SVC(kernel='linear')
num_samples = 10000
classifier.fit(features_train[0:num_samples], labels_train[0:num_samples])
predictions = classifier.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)

t0 = time()
classifier.fit(features_train[0:num_samples], labels_train[0:num_samples])
print "training time:", round(time()-t0, 3), "s"

t0 = time()
classifier.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"
#
#########################################################

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
classifier = svm.SVC(kernel='linear')
classifier.fit(features_train, labels_train)
predictions = classifier.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)

#########################################################

for i in [10, 100, 1000, 10000]:
    classifier = svm.SVC(kernel='rbf', C=i)
    classifier.fit(features_train, labels_train)
    predictions = classifier.predict(features_test)
    # 0.8924914675767918
    print(accuracy_score(labels_test, predictions))

classifier = svm.SVC(kernel='rbf', C=10000)
classifier.fit(features_train, labels_train)
predictions = classifier.predict(features_test)
# 0.8924914675767918
print(accuracy_score(labels_test, predictions))

for prediction in [10, 26, 50]:
    print(predictions[prediction])

from collections import defaultdict
result = defaultdict(int)
for prediction in predictions:
    result[prediction] += 1

print result


