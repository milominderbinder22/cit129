# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 01:40:43 2018

"""

import urllib, json, webbrowser, requests
from bs4 import BeautifulSoup

apiKey="NFXEysI5tWN2ehm3P2OjpGSMV4L8DLEJ"

#searchTerm="ryan+gosling"
searchTerm="puppies"
searchLimit=5

p="http://api.giphy.com/v1/gifs/search?q="+searchTerm+"&api_key="+apiKey+"&limit="+str(searchLimit)

## FOR TRENDING:  https://api.giphy.com/v1/gifs/trending?api_key=
##NFXEysI5tWN2ehm3P2OjpGSMV4L8DLEJ&limit=25&rating=G"

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
    
    ##print finalURL, just for monitoring
    ##print(finalURL)
        
    return finalURL

def writeHTML(listOfURLS):
    ## writes an HTML file 
    htmlStart="<html><table>"
    htmlEnd="</table></html>"
    htmlGuts=""
    tdCounter=0
    ##trStartTag=""
    ##trEndTag=""
    for i in listOfURLS:
        trStartTag=""
        trEndTag=""
        if tdCounter%2==0:
            trStartTag="<tr>"
        elif tdCounter%2==1:            
            trEndTag="</tr>"
        htmlGuts=htmlGuts+trStartTag+"<td><img src=\""+i+"\" alt=\"animated\" /></td>"+trEndTag
        tdCounter +=1
    ##print("HtmlGuts is: ",htmlGuts)
    htmlString=htmlStart+htmlGuts+htmlEnd
    
    with open("testGifHTML.html","w") as outfile:
        outfile.write(htmlString)
    

"""
CONTROL BELOW:
"""
## requests JSON
req=urllib.request.Request(p)
with urllib.request.urlopen(req) as response:
    mypage=response.read()
result=json.loads(mypage)

##print the JSON to a file
printJSON(mypage)

## select the particular image size we want of our gifs, and how many
gifURLS=[]
for i in range(searchLimit):
    bitly_url=result["data"][i]["bitly_gif_url"]
    ##NOTE: COULD MAKE THE SIZE OF THE GIF A VARIABLE IN LINE ABOVE
    ## i.e. different size formats
    print("bitly_url%s is: "%str(i),bitly_url)
    ## we've got the bitly_url.
    ## but, it redirects to a page of GIF's
    ## so call a method to deal with that...    
    finalURL=getParticularGIF(bitly_url)
    
    print("finalURL is: ",finalURL)
    
    gifURLS.append(finalURL)
    
writeHTML(gifURLS)

    
    
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