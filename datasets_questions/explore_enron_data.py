#!/usr/bin/python

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print enron_data['KENETH LAY L']

counts_poi=[0,0]
for key, d in enron_data.iteritems():
     if d['poi'] == 'NaN' and d['poi'] == True:
             counts_poi[0] += 1
     elif d['poi'] == True:
             counts_poi[1] += 1
             

#print enron_data["PRENTICE JAMES"]["total_stock_value"]
#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print (enron_data["SKILLING JEFFREY K"]["total_payments"])
print (enron_data["LAY KENNETH L"]["total_payments"])
print (enron_data["SKILLING JEFFREY K"]["total_payments"])

#print counts_poi