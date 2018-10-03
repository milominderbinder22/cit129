# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:42:46 2018

"""

def jailRaceStats(filename,date):

    file = open(filename,'r',newline='')

    data=zip()

    header = []
    dates = []
    race = []
    desiriDatum=date

    totalCount=0
    numberWhites=0
    numberBlacks=0

    lineCounter=0

    for line in file:
        line=file.readline()
    
        if lineCounter==0:
            firstLine=line.split(',')
            for j in firstLine:
                header.append(j)
    
        if lineCounter>0:
            splitLine=line.split(',')
            for j in splitLine:
                if j == desiriDatum:
                    dates.append(j)
                elif j == 'B':
                    race.append(j)
                elif j == 'W':
                    race.append(j)
        lineCounter += 1

    data=zip(dates,race)

    for values in data:
        ##print(values)
    
        if values[1]=='B':
            numberBlacks += 1
        elif values[1]=='W':
            numberWhites += 1
    
        totalCount += 1
    
    print("On %s:"%desiriDatum)
    print("\tThe black population was: " + str(numberBlacks))
    print("\tThe white population was: " + str(numberWhites))
    print("\tThe total inmate count was: " + str(totalCount))
    print()
    print("Blacks represented %.2f percent of the total population"%(numberBlacks*100/totalCount))
    print("Whites represented %.2f percent of the total population"%(numberWhites*100/totalCount))



jailRaceStats('jail.csv','2016-03-17')

##scraps and snippets:
##print("And the third entry is:\n")
##print(values(4))

##print("And the header is: " + str(header))
##print(len(header))
##print(type(header))
    
## passing arg to readline(n) reads first n chars of line
##firstLine=file.readline(5)  