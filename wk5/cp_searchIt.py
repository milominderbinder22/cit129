# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:37:21 2018


"""

import json

def getCriteria(filename):
    with open(filename,'r') as infile:
        criteria=json.load(infile)

    return criteria

def printProject(n):
    keys=n.keys()
    for i in keys:
        print(i + ": ",n[i])
    print("--------------------------")
    
##def checkCriteria(item,criteria): ##deprecated, too many calls
def extractCriteria(criteria):
            
    asset_type=[]
    fiscal_year=[]    
    status=[]
    area=[]
    start_date=[]
    ## TO ADD ADDITIONAL CRITERIA: create a list for each criteria HERE
    
    for i in criteria:
        if i=="asset_type":
            for j in range(len(criteria[i])):
                asset_type.append(criteria[i][j])
        if i=="fiscal_year":
            for j in range(len(criteria[i])):
                fiscal_year.append(criteria[i][j])
        if i=="status":
            for j in range(len(criteria[i])):
                status.append(criteria[i][j])
        if i=="area":
            for j in range(len(criteria[i])):
                area.append(criteria[i][j])
        if i=="start_date":
            for j in range(len(criteria[i])):
                start_date.append(criteria[i][j])
        ## TO ADD ADDITIONAL CRITERIA: add a list populator of the form above HERE
                
                
    return(asset_type,fiscal_year,status,area,start_date)            
    #TO ADD ADDITIONAL CRITERIA: add the new criterion's list name 
    ##to the return statement above            


def searchCP(criteriaFileName,CPfilename): #should also take CPfilename
    
    asset_typisch=[]
    fiscal_year=[]
    status=[]
    area=[]
    start_date=[]
    
    criteria=getCriteria(criteriaFileName)
    
    counter=0
        
    with open(CPfilename,'r') as datafile:
        data=json.load(datafile)
    
    asset_typisch,fiscal_year,status,area,start_date = extractCriteria(criteria)
        
    for p in data['features']:
        if len(asset_typisch)>0 and p['properties']['asset_type'] not in asset_typisch:
            continue
        elif len(fiscal_year)>0 and p['properties']['fiscal_year'] not in fiscal_year:
            continue
        elif len(status)>0 and p['properties']['status'] not in status:
            continue
        elif len(area)>0 and p['properties']['area'] not in area:
            continue
        elif len(start_date)>0 and p['properties']['start_date'] not in start_date:
            continue
        ##TO ADD ADDITIONAL CRITERIA: add the new criterion's list name
        ## in a statement with the form immediately above
        else:
            counter +=1
            printProject(p['properties'])
            
        ## COULD ALSO WRITE THESE TO A FILE. USING A METHOD.
            
    
    print("Asset type list is: ",asset_typisch)
    print("And fiscal yr is: ",fiscal_year)
    
    print(str(counter)+" such projects") 
    ##gives count of projects found meeting criteria
    
    
        
#execution control below:
        
searchCP('cp_search_criteria.json','cgcapitalprojects_img.geojson')

""" 

    SNIPPETS AND NOTES AND SUCH:
    
    if contains "fiscal\w" "asset\w" etc then do that thing (regex)


"""



    
    
    