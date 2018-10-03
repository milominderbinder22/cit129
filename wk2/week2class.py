# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:23:06 2018

@author: puter
"""

def countTo100():
    for i in range(101):
        if i%2!=0:
            print(i,end="")
        else:
            continue

def accentuate(s):
    for char in s:
        for i in range(3):
            print(char,end=" ")
        ## this end = " " is the difference between console printing it 
        ## all on one line, or each letter on a separate line

def everyOther(s):
    print(s[::2])
    
    ##for char in s[::2]:
        ##print(s,end=" ")

def crazyMath():
    ##for i in range(1,5,1):
      ##  for j in range(5,8,1):
      ##      for k in range(5,8,1):
      ##          print(str(i)+"|"+str(j)+"|"+str(i*k))
                
      for i in range(1,5,1):
          for j in range(5,8,1):
              print(str(i)+"|"+str(j)+"|"+str(i*j))


def properLabeller():

    listoflists=[['mn','pa','ut'],['b','p','c'],['echo','charlie','tango']]
    labels={"state":"US State Abbr: ","element":"Chemical Element: ","alpha":"Phonetic Call: "}
        
    for i in listoflists:
        for j in range(len(i)):
            if len(i[j])==2:
                print("%(state)s"%labels,i[j])
            elif len(i[j])==1:
                print("%(element)s"%labels,i[j])
            else:
                print("%(alpha)s"%labels,i[j])
                
"""for i in listoflists:
    for j in range(len(i)):
        if len(i[j])==2:
            print(labels["state"],i[j])
        if len(i[j])==1:
            print(labels["element"],i[j])
        else:
            print(labels["alpha"],i[j])
"""    
        
##crazyMath()
##countTo100()
##accentuate("kaboom")
##everyOther("askaliceithinkshe\'llknow")
##properLabeller()            

def dictExplorer(d):
    """ should take a dictionary as an argument
    possibly take the dictionary from a file
    or from a path
    or from the web or git"""
    
    
    



