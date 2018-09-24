# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:30:56 2018


"""

import csv
# this is on the site

#create data aggregation variables for use in my looping
totalBlackInmates=0
totalWhiteInmates=0
totalCount=0

# open jail census file
file=open('jail.csv',newline='')
reader=csv.DictReader(file)

# read in file one line at a time
# retrieving each row as a dict
for row in reader:
    if row['Date']=='2016-03-17':
        totalCount+=1
        if row['Race']=='B':
            totalBlackInmates+=1
        if row['Race']=='W':
            totalWhiteInmates+=1
file.close()

# examine a row, based on values for 
# race, increment, aggregate counters

# display final values of aggregation variables
print("Total black inmates: %i" % totalBlackInmates)
print("Total white inmates: %i" % totalWhiteInmates)
print("Total count: %i"%totalCount)
print("Black percentage: %f"%(totalBlackInmates*100/totalCount))