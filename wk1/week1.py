# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 00:09:58 2018

@author: puter
"""

def countTo():
    userInput=input("Please enter the upper list bound: ")
    userList=[]
    for i in range(int(userInput)):
        userList.append(i)
    print("The list is: \n" + str(userList))
    total=0
    for i in range(int(userInput)):
        total+=i
    print("\n")
    print("The total of the list is: \n" + str(total))
    
##countTo()
    
def getInput():
    userInput=str(input("Please enter a string of at least 4 chars:\n"))
    if len(userInput)<4:
        print("Sorry.  Not long enough.")
        return null
    else:
        return userInput

        
def firstLast():
    userInput=getInput()
    if userInput != 'null':
        print("The magic combo is:\n")
        print(userInput[0]+userInput[1]+userInput[-2]+userInput[-1])
            

def isMagicWord():
    userInput=getInput()
    if userInput[1]==userInput[-2]:
        print("Abracadbra!")
    else:
        print("That is not a magic word!")
        
def threeStrings():
    input1=getInput()
    input2=getInput()
    input3=getInput()
    
## maybe create a dictionary here?  input1:length, etc??
## then fetch entry with longest?
## could also do recursively?
    
## also:  what is NumPy Series (as suggested on StackOverflow)?  
## pandas.Series.order

    words={input1:len(input1),input2:len(input2),input3:len(input3)}
    ##sortedWords=sorted(words.values())
    sortedWords=sorted(words,key=words.get)
    print(sortedWords)
    ##returns a list!!!
    for i in sortedWords[::-1]:
        print(i)
        ## how would one elegantly get it all on one line?
                  

##firstLast()
##isMagicWord()
threeStrings()

