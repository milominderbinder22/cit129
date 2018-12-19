# -*- coding: utf-8 -*-
"""
A BRIEF TUTORIAL ON PYTHON CLASSES AND OOP

"""

class person:
    def __init__(self,name="",gender="",birthday=""):
        self.name=name
        self.gender=gender
        self.birthday=birthday
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getBirthday(self):
        return self.birthday
    
    ## NOTE: the __init__() method is called a CONSTRUCTOR
    ## it builds the INSTANCE from the class "blueprint"
    
    ## 
    
me= person("Jeff","M","04/16/1975")
## NOTE: the 'self' in pythonspeak is "me" in this case

## print(me) will tell us that me is a person object
print(me)
print("--------------------------")

## there are a couple of ways to fetch data from an object:
print("My gender is:",me.getGender())
print("My gender is still:",me.gender)
print("Oh.  And my name is",me.getName())
print("Remember.  That's",me.name.upper())
print("----------------------------")

## You can also define set() methods to change the attributes in an object
## Variables are called "attributes" in OOP, btw
## or, you can change your attributes like this:

me.name="Jorge"

## So... did it work?  Let's see.

print("But henceforth, I shall be known as",me.getName())
print("-------------------------------")
## making a class "private" will prevent such overwriting, 
## which would NECESSITATE the set() method being defined

## anyway... it's pretty much boilerplate for python classes
## to have getter and setter methods for their variables 
## And remember, variables are called "ATTRIBUTES" in OOP

## Now, let's make subclass.
## It will be called employee.  
## And it will INHERIT from the person class we made above.

class employee(person):
    ## cause employees are people, too
    def __init__(self,
                 name,
                 gender,
                 birthday,
                 job="",
                 ID="",
                 salary=""):
            ## employees get job titles and ID's and stuff.  
            ## So let's set those:
            self.job=job
            self.ID=ID
            self.salary=salary
            ## this next line is important.  We'll come back to why in a bit.
            super().__init__(name,gender,birthday)
            
            ## we'll also discuss what this 'self' business is as we go
    
    def printStatement():
        print("does this do anything")
    
    def getJob(self):
        return self.job
    def getID(self):
        return self.ID
    def axe(self):
        self.job="Sacked"
        self.salary="Yeah, right."
    def calculateWitholding(self):
        return int(self.salary)*.22
    
jeff=employee("Jeffrey Perkosky","M","04/16/1975","CEO","1","32000000")
## in pythonspeak, the "self" is now "jeff" in this case
## in other words, "self" is whatever you name your INSTANCE

## let's check the attributes (variables) of the jeff instance
print(jeff.getName())
print(jeff.job)
print(jeff.birthday)
print("---------------------")

## wait a minute!  when we made the jeff employee object
## we gave it all that info (name and birthday and job and such).

## BUT the employee class doesn't have any self.birthday or self.name setters
## what gives?

## It's called INHERITANCE.  The employee object is INHERITING the structure
## from its SUPERCLASS (person).
## And that's why we set those attributes with the super()__init__() method.

## So jeff is an employee.  And therefore he is a person.
## but "me" is a person, and not an employee.
## Just watch what happens when I try to print me.job

##print(me.job)

## And speaking of methods()... we've got some methods to play with:
## Let's discuss Jeff's tax bracket

jeffTaxes = jeff.calculateWitholding()
print("Jeff's witholding is:$%.2f"%jeffTaxes)
print("---------------------------------")

## That's his TAX BILL?!  What're we paying this guy for, his personality?!
## Let's fire jeff.  We've got a METHOD for that.
jeff.axe()

## Let's check on Jeff's career outlook now:
print("Jeff's position with the firm is:",jeff.job)
print("Jeff's current salary is:",jeff.salary)
print("-------------------------")

employee.printStatement()

"""
"""


