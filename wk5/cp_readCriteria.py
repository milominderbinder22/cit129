# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:37:21 2018


"""

import json

def getCriteria(filename):
    with open(filename,'r') as infile:
        criteria=json.load(infile)

    """for i in criteria:
        print(i,criteria[i])"""

    return criteria

def printProject(n):
    keys=n.keys()
    for i in keys:
        print(i + ": ",n[i])
    print("--------------------------")
    
##def checkCriteria(item,criteria):
def extractCriteria(criteria):
    
    include=False
    
    """for i in criteria:
        if isinstance(criteria[i],list):
            ##print("That's a list")
            print(i)"""
            
    asset_type=[]
    fiscal_year=[]    
    status=[]
    area=[]
    start_date=[]
    
            
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
                
                
    return(asset_type,fiscal_year,status,area,start_date)            
                
    ##print(asset_type)
    ##print(fiscal_year)
    
            
        

    
    
    """if item['asset_type']==criteria['asset_type']:
        include=True"""
    
    ##return include

##if contains "fiscal\w" "asset\w" etc then do that thing

def searchCP(criteriaFileName,CPfilename): #should also take CPfilename
    
    asset_typisch=[]
    fiscal_year=[]
    status=[]
    area=[]
    start_date=[]
    
    criteria=getCriteria(criteriaFileName)
    
    counter=0
    
    """for i in criteria:
        print(i,criteria[i])"""
        
    with open(CPfilename,'r') as datafile:
        data=json.load(datafile)
    
    asset_typisch,fiscal_year,status,area,start_date = extractCriteria(criteria)


## I want to split this off into its own method, and keep calling it
## with different fields, in turn (i.e first asset_type,
## then if true, call with the fiscal_year, then if true
## call with status, etc, until it's false, or we print)
    
    
    
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
        else:
            counter +=1
            printProject(p['properties'])
        
            
    """
    if checkCriteria(p['properties'],criteria)==True:
        counter +=1
        printProject(p['properties'])"""
            
    
    print("Asset type list is: ",asset_typisch)
    print("And fiscal yr is: ",fiscal_year)
            
    
    print(str(counter)+" such projects")
    
    
        
        
        
#control:
        
searchCP('cp_search_criteria.json','cgcapitalprojects_img.geojson')



    
    
    