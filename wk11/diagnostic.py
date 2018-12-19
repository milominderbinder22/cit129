# -*- coding: utf-8 -*-

userLength=int(input("Please enter a positive integer: "))
print(userLength)


with open("wordList.rtf", "r") as infile:
    matchingLength = []
    for line in infile:
        strippedLine=line.rstrip('\n')
        strippedLine2=strippedLine.rstrip('\par')
        
        if len(strippedLine2)==userLength:
            matchingLength.append(strippedLine2)
        print(matchingLength)

"""
    for line in infile:
        if len(line)==userLength:
            array.append(line)

print(array)
"""

"""
with open("wordList.rtf", "r") as infile:
    
    lines=infile.readlines()
    for line in lines:
            print(line)
"""
    