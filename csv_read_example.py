#!/usr/bin/env python

"""
Simple demo of using data_support.read.csv to read test data from a 
csv file.
"""

import random
import data_support

# Read data from file
test_data = data_support.read_csv("rep_order_date_and_mags_court.tsv")

# Display all the read data
print "All Rows"
for ri, row in enumerate(test_data):
    print "\nRow", ri
    for k, v in row.iteritems():
        print k+":", v
        
#Indivdual item
print ""
print "Row chosen at random"
chosen_row = random.choice(test_data)
print "Court:", chosen_row.get("mags_court")
print "Date:", chosen_row.get("reporder_date")
#Other way of accessing 
##print chosen_row["mags_court"]