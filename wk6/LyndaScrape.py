# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:42:46 2018

@author: puter
"""

"""
import urllib
from bs4 import BeautifulSoup
p="https://www.goodreads.com/search?q=python"
##"ftp://www.goodreads.com"
req=urllib.request.Request(p)
with urllib.request.urlopen(req) as response:
    the_page=response.read()
soup=BeautifulSoup(the_page,'html.parser')    
res=soup.find_all('a',class_='bookTitle')
##res=soup.find_all('a',)
##print(res)
for item in res:
    t=item.find('span').string
    print(t)
##could build workflow around methods: by def generateSearchURL that gets built up by arguments to search for
"""

import urllib
from bs4 import BeautifulSoup

p="https://www.lynda.com/search?q=python"
req=urllib.request.Request(p)
with urllib.request.urlopen(req) as response:
    mypage=response.read()
soup=BeautifulSoup(mypage,'html.parser')

res=soup.find('cite')
print(res.next_sibling)
## need to examine the BS doc's for class type to understand
## how to iterate over it



    