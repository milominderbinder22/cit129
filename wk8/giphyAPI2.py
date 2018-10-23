# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 01:40:43 2018

"""

import urllib, json, webbrowser, requests
from bs4 import BeautifulSoup

with open('giphyAPIkey.txt','r') as infile:
    apiKey=infile.read()

## put this up a directory, a la coral's trick

#searchTerm="ryan+gosling"
searchTerm="simpsons"
searchLimit=300

## tried to make a variable to hold the gif type we'd like to extract...
## (but it didn't work this way)
##sizeOfGIF="[\"images\"][\"downsized\"][\"url\"]"

queryTerm="http://api.giphy.com/v1/gifs/search?q="+searchTerm+"&api_key="+apiKey+"&limit="+str(searchLimit)
trending="https://api.giphy.com/v1/gifs/trending?api_key="+apiKey+"&limit="+str(searchLimit)+"&rating=G"

def printJSON(mypage):
    result=json.loads(mypage)
    with open('giphyJSON.json','w') as outfile:
        outfile.write(json.dumps(result,sort_keys=True,indent=4))

def getParticularGIF(bitly_url):
    ##pull the bitly_url page into a response object
    req=urllib.request.Request(bitly_url)
    with urllib.request.urlopen(req) as response:
        mypage=response.read()
    ## then make some BeautifulSoup out of that object
    soup=BeautifulSoup(mypage,'html.parser')
    ##now, find the tag we want
    gifRes = soup.find('meta',attrs={"property":"og:url"})
    ##find the direct https:// URL from the tag.  Call it finalURL
    finalURL=gifRes['content']
    ## 'content' is tag attribute we're interested in, btw
        
    return finalURL

def writeHTML(listOfURLS,listOfTitles):
    ## writes an HTML file
    
    htmlStart="<html><body bgcolor=\"#2F0FFF\"><table style=\"width:100%\">"
    htmlEnd="</table></body></html>"
    htmlGuts=""
    tdCounter=0
    ##trStartTag=""
    ##trEndTag=""
    titleCounter=0
    for i in listOfURLS:
        trStartTag=""
        trEndTag=""
        if tdCounter%5==0:
            trStartTag="<tr>"
        elif tdCounter%5==4:            
            trEndTag="</tr>"
        htmlGuts=htmlGuts+trStartTag+"<span title=\""+listOfTitles[titleCounter]+"\"><img src=\""+i+"\" alt=\"animated\" /></span>"+trEndTag
        tdCounter +=1
        titleCounter +=1
    ##print("HtmlGuts is: ",htmlGuts)
    htmlString=htmlStart+htmlGuts+htmlEnd
    
    with open("testGifHTML.html","w") as outfile:
        outfile.write(htmlString)
    

"""
CONTROL BELOW:
"""
## requests JSON
##def getMeSomeGifs(typeOfGifs,numberOfGifs):
    
req=urllib.request.Request(trending)
with urllib.request.urlopen(req) as response:
    mypage=response.read()
result=json.loads(mypage)

##print the JSON to a file
printJSON(mypage)

## select the particular image size we want of our gifs, and how many
gifURLS=[]
gifTitles=[]
for i in range(searchLimit):
    url=result["data"][i]["images"]["fixed_height"]["url"]
    title=result["data"][i]["title"]
    ##url=result["data"][i]["images"]["downsized"]["url"]
    ##NOTE: COULD MAKE THE SIZE OF THE GIF A VARIABLE IN LINE ABOVE
    ## i.e. different size formats
    ##print("bitly_url%s is: "%str(i),bitly_url)
    ## we've got the bitly_url.
    ## but, it redirects to a page of GIF's
    ## so call a method to deal with that...    
    ##finalURL=getParticularGIF(bitly_url)
    
    ##print("finalURL is: ",finalURL)
    
    gifURLS.append(url)
    gifTitles.append(title)
    
writeHTML(gifURLS,gifTitles)



"""
FRAGMENTS AND SNIPPETS:
    
## ok, so loop through however many times/items you want, and write
## each gif to a file in wb format
## then, build a table in HTML programatically, using beautifulSoup

## I initially just popped open a web browser when I retrieved a bitly_url: 
webbrowser.open(bitly_url), like so...

with open('gifFile2.gif','wb') as outfile:
    outfile.write(requests.get(bitly_url).content)

## useful for formatting JSON in a file...
data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key="+apiKey+"&limit=5").read())
print(json.dumps(data,sort_keys=True,indent=4))
"""

"""
    ## now open our final .gif destination as a url request object
    req2=urllib.request.Request(finalURL)
    with urllib.request.urlopen(req2) as response:
        mypage2=response.read()
"""
    
##write the .gif to a file, in binary mode (wb)
"""with open('gifFileTester.gif','wb') as outfile:
    outfile.write(mypage3)
"""