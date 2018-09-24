# -*- coding: utf-8 -*-
"""

"""

## the two methods, getLine() and printGreeting() work together
## getLine() takes as arguments: a filename (assumed to be in the working directory), 
    ##and the number of a particular line to read and return
## printGreeting() takes as arguments: a filename, and a number of total lines to read from that file
## printGreeting() calls getLine() with the filename, and with each line up to and including the number of
    ## lines that printGreeting() is told to read
## printGreeting() then prints a greeting for each name on a line in the target file 
    ##using format lastname, firstname
## notes: getLine closes and opens the file every time it retrieves a single line
## maybe a way to avoid that?

def getLine(filename,lineNumber):
    newFile=open(filename,'r')
    
    for i in range(lineNumber):
        line=newFile.readline()
    
    newFile.close()
    
    return line

      
def printGreeting(filename,numberOfEntries):
    
    for i in range(numberOfEntries):
        currentLine=getLine(filename,i+1)
        splitString=currentLine.split()
        print("Good evening Dr. " + splitString[1] + ", would you mind if I called you " + splitString[0] + "?")
        ##print("Hiya, ",currentLine)

printGreeting('names.txt',4)
    
##testLine=getLine('names.txt',4)
##print("TestLine is: ",testLine)



