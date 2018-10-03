# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:20:13 2018

@author: puter
"""
##from termcolor import colored
from colorama import Fore
from colorama import Style

cryptos={
        ##can put a non-dictionary element in here to test
        'test':'this is a test',
        'test2':'this is ALSO a test',
        'test3':'yet another test',
        
        'platforms':
            {
            'description':'can make stuff out these',
            'eth':{'name':'Ethereum','year':2014,'priceUSD':193},
            'ada':{'name':'Cardano','year':2016,'priceUSD':.06},
            'eos':{'name':'EOS','year':2017,'priceUSD':4.85},
            'neo':{'name':'NEO','year':2014,'priceUSD':17.49}
                    
            },
            
        'computing, data management, and cloud services':
            {
            'description':'paradigm shifters',
            'gnt':{'name':'Golem','year':2016,'priceUSD':.12},
            'sia':{'name':'Siacoin','year':2015,'priceUSD':.01},
            'storj':{'name':'Storj','year':2015,'priceUSD':.23},
            'hot':{'name':'Holotoken','year':2017,'priceUSD':.001}
            },
            
        'payments':
            {'description':'you can pay for stuff with these',
             'ltc':{'name':'Litecoin','year':2011,'priceUSD':51.00},
             'etn':{'name':'Electroneum','year':2016,'priceUSD':.0051},
             'nano':{'name':'NANO','year':2014,'priceUSD':2.05},
             'doge':{'name':'Dogecoin','year':2013,'priceUSD':.01}
            }
        
        
        }
            
def dictExplorer(d):
   
    top=d.keys()
    print("First level of dict has " + str(len(top)) + " keys (dicts in red):")
    for i in top:
        if isinstance(d[i],dict):
            print(f'{Fore.RED}'+i+f'{Style.RESET_ALL}',end=" | ")
        else:
            print(i,end=" | ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    for i in top:
        if isinstance(d[i],dict):
            print("Dictionary: " + i)
            second=d[i].keys()
        ##second=d[i].keys()
            print("\t ...contains: " + str(len(second)) + " keys (dicts in blue):")
            for j in second:
                if isinstance(d[i][j],dict):
                    print(f'{Fore.BLUE}'+j+f'{Style.RESET_ALL}',end=" | ")
                else:
                    print(j,end=" | ")
            print("\n with dict keys:values:")
            
            for j in second:
                if isinstance(d[i][j],dict):
                    print(d[i][j])
                else:
                    continue
            print("--------------------------------------")

    getInput(d)            
            
##viewDict() will fetch/call dictExplorer()

    ##print(d['payments']['ltc'])            
            
def getInput(d):
    userInput=str(input("Enter:\n1 to view dictionary\n2 to get entry\n3 to delete a value\n86 to exit\n"))
    if userInput=="1":
        dictExplorer(d)
    if userInput=="2":
        fetchEntry(d)
    if userInput=="3":
        deleteValue(d)
    if userInput=="4":
        d.items()

def fetchEntry(d):
    done='false'
    while done=='false':
        
        userInput=str(input("Enter a key or dict\nOr 86 to exit"))
        
        if userInput=='86':
            done='true'
            
def deleteValue(d):
    ##dictCopy=
    ##toDelete=str(input("Enter the 'path' to the dictionary value to delete, separated by commas\n"))
    
    top=d.keys()
    print("First level of dict has " + str(len(top)) + " keys (dicts in red):")
    for i in top:
        if isinstance(d[i],dict):
            print(f'{Fore.RED}'+i+f'{Style.RESET_ALL}',end=" | ")
        else:
            print(i,end=" | ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    selection=str(input("Type the key that you'd like to delete or explore:\n"))
    
    if isinstance(d[selection],dict):
        print("That's a dictionary.")
        
        for i in d[selection]:
            if isinstance(d[selection][i],dict):
                print("Dictionary: " + i)
                second=d[selection][i].keys()
                ##second=d[i].keys()
                print("\t ...contains: " + str(len(second)) + " keys (dicts in blue):")
                for j in second:
                    if isinstance(d[selection][i][j],dict):
                        print(f'{Fore.BLUE}'+j+f'{Style.RESET_ALL}',end=" | ")
                    else:
                        print(j,end=" | ")
                print("\n with dict keys:values:")
            
                for j in second:
                        print(d[selection][i][j])
                        
                for j in second:
                    ##print(d[selection][i][j].get(),":" + d[selection][i][j])
                    print(d[selection][i])
                    """selection2=str(input("Type the key that you'd like to delete or explore.\n"))
                    if isinstance(d[selection][selection2]):
                        print("That's ALSO a dictionary!")
                    else:
                        dictCopy=d.copy()
                        del d[selection][selection2]
                        getInput(dictCopy)"""
                
        selection2=str(input("Type the key you'd like to delete.\n"))
        dictCopy=d.copy()
        del dictCopy[selection][selection2]
        getInput(dictCopy)
                
                
                
        """else:
                continue"""
                
        ##print("--------------------------------------")
        
##here       
        
    else:
        confirm=str(input("That's not a dictionary.  Delete its value? y/n\n"))
        if confirm=='y':
            dictCopy=d.copy()
            del dictCopy[selection]
            getInput(dictCopy)
            
        elif confirm=='n':
            print("not deleting, sir!")
        else:
            deleteValue(d)
    
def getTopLevel(d):
    return

            
    
##a=cryptos.items()
##print(a)
##print(type(a))
##b=cryptos.copy()
##print(b)
##print(type(b)) 
    
getInput(cryptos)  
##dictExplorer(cryptos)


"""CUT CODE SNIPPETS:"""

"""for i in range(len(top)):
        second=i.keys()
        print("second level of dict has: " + str(len(second)) + " keys.")"""
        
"""for i in top:
        second=d[i].keys()
        print("key: " + i + " contains: " + str(len(second)) + " keys.")
        for j in second:
            if type(d[i][j])=='dict':
                print(d[i][j])
                print(type(d[i][j]))
            else:
                continue"""
        
        
"""for j in second:
            third=d[i][j].keys()
            print("key: " + j + "contains: " + str(len(third)) + "keys.")"""
    
##print("%d of them are dictionaries",k)            