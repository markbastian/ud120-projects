#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# len(enron_data)

import re

re.match(r"LAY", "LAY, KENNETH")
filter(lambda n : re.match(r"LAY", n), enron_data.keys())

len(filter(lambda (k, v) : v["poi"] == 1, enron_data.items()))

for k,v in enron_data.items():
    if re.match(r"LAY|SKILLING|FASTOW", k):
        print(k + ':\t' + str(v['total_payments']))

salaries = 0

for k, v in enron_data.items():
    if v['salary'] != 'NaN':
        salaries += 1

emails = 0

for k, v in enron_data.items():
    if v['email_address'] != 'NaN':
        emails += 1

payments = 0

for k, v in enron_data.items():
    if v['total_payments'] != 'NaN':
        payments += 1

for k, v in enron_data.items():
    if v['total_payments'] == 'NaN' and v['poi'] == True:
        payments += 1

len(filter(lambda (k, v) : v['poi'] == True, enron_data.items()))

len(filter(lambda (k, v) : v['total_payments'] == 'NaN' and v['poi'] == True, enron_data.items()))

len(filter(lambda (k, v) : v['total_payments'] == 'NaN', enron_data.items()))

