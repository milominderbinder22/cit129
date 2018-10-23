# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:42:46 2018

"""

## possible place to take this: build workflow around methods: 
## by def generateSearchURL that gets built up 
## by arguments to search for

import urllib, json
from bs4 import BeautifulSoup

## notes on testing:
## WORKS: python, linux, amazon
## WORKS, BUT WEIRDLY: c, math
## NOT AT ALL: calculus, statistics, aws, AWS
searchTerm = "python"
p="https://www.lynda.com/search?q="+searchTerm
req=urllib.request.Request(p)
with urllib.request.urlopen(req) as response:
    mypage=response.read()
soup=BeautifulSoup(mypage,'html.parser')

##res=soup.find_all('cite')
##print(res[0].find_next_siblings("div"))
descriptionRes = soup.find_all('div',attrs={"class":"meta-description hidden-xs"})
## now that I think about it, I actually wouldn't mind a method
## to find a specified number of courses, not just "all"

coursesFound={}


numberOfCourses=len(descriptionRes)
counter=0
for i in descriptionRes:
    ##descriptionRes is of type bs4.element.ResultSet
    ##it is composed of tags: i.e. type= bs4.element.Tag
    ## so i in the current for loop represents these tags
    if counter<5:
        
        instructorRaw=i.find_previous('cite',attrs={"class":"meta-author"})
        instructor=instructorRaw.text.strip("with ")
        descriptionRaw=i
        description=descriptionRaw.text
        durationRaw=i.find_next('span',attrs={"class":"meta-duration"})
        duration=durationRaw.text
        levelRaw=i.find_next('span',attrs={"class":"meta-level"})
        level=levelRaw.text
        viewsRaw=i.find_next('span',attrs={"class":"meta-views hidden-xs"})
        views=viewsRaw.text.strip("Views: ")
        
        print("Instructor: "+instructor)
        
        print("Description: "+description)
        
        if duration !="":
            print("Duration: "+duration)
        
        if level !="":
            print("Level: "+level)
        
        if views !="":
            print(views)
        print("---------------------------")
        
        thisCourse={}
        ##thisCourse['Description']=description
        thisCourse['Instructor']=instructor
        thisCourse['Duration']=duration
        thisCourse['Level']=level
        thisCourse['Views']=views
        
        coursesFound[description]=thisCourse
        
    counter+=1
    ##print(type(i))

## maybe try/catch "attribute error" or just catch all errors and continue

print(len(descriptionRes))
print(coursesFound)

with open('lyndaCourse.json','w') as outfile:
    json.dump(coursesFound,outfile)
##print(courses)
##print(type(descriptionRes))

## to do: distinguish "courses" from "videos"
## to do: check for null values in duration, level, instructor, etc
## to do: print to file, json, or csv

"""
SNIPPETS AND FRAGMENTS:

##print(i.find_next("div").text)
##durLvlViews=i.find_next("div").text
##print(durLvlViews)
##print(type(durLvlViews))

##print(res[counter].find_next_siblings("div"))
##div=res[counter].find_next_siblings("div")
##print(div)
##text=div.contents[0]
##print(i.find.previous("h2").text)
##print(i.find_previous("cite").text)

## the code below doesn't work, and I REALLY wanna know why!
counter=0
for i in res:
    if counter<5:
        print(i.find_next_siblings("div").text)
        print("--------------------")
    counter += 1
##citation=soup.find('cite')
##print(citation)
##print(citation.find_next_siblings("div"))

##print(res.next_sibling)
## need to examine the BS doc's for class type to understand
## how to iterate over it

##import urllib2
import urllib
from bs4 import BeautifulSoup

coursePage="https://www.lynda.com/search?q=python"
page = urllib.urlopen(coursePage)
soup = BeautifulSoup(page,'html.parser')
citations=soup.find_all('cite')
for i in citations:
    print(i)
"""
