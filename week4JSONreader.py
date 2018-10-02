# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:18:44 2018

"""

import json

f=open('cgcapitalprojects_img.geojson','r')
res=json.load(f)

"""for p in res['features']:
    printProject(p['properties'])
    assembleAreaList(p['properties'])
    if p['properties']['area']=='':
        logMalformedProject(p['properties'])
    print(areas)
"""

def printProject(n):
    ##print(n)
    ##print(type(n))
    ##print(n.keys())
    keys=n.keys()
    ##print(keys)
    ##print(type(keys))
    for i in keys:
        print(i +": ",n[i])
        
def logMalformedProject(n):
    malCounter=0
    if n['area']=="":
        l=open('errorLog.txt','a')
        l.write(str(n['id']))
        l.close()
        
        return True;
    
def checkAreaType(l,n):
    types=[]
    if str(n['area']) not in l:
        l.append(n['area'])
    return l    

##control below:    
malCounter=0
types=[]
for i in res['features']:
    ##if counter==3:
    printProject(i['properties'])
    mal=logMalformedProject(i['properties'])
    ##counter += 1
    if mal:
        malCounter +=1
    types=checkAreaType(types,i['properties'])
    print("------------------------------")
    

print("There were " +str(malCounter)+ " malformed projects found.")
print("The area fields have types :" + str(types))

##print(malCounter)


"""for i in res['features']:
    ##print(res['features'].keys())
    if counter==2:
        print(i['properties'])
    counter += 1"""

## snippets and fragments below:
    
##print(type(res['features']))
## ...so features is a list

##counter=0
##print(type(res))


    
    