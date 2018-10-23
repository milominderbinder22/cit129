# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 00:33:19 2018


"""

import unirest

response = unirest.get("https://indeed-indeed.p.mashape.com/apisearch?publisher=&callback=<required>&chnl=<required>&co=<required>&filter=<required>&format=json&fromage=<required>&highlight=<required>&jt=<required>&l=austin%2C+tx&latlong=<required>&limit=<required>&q=java&radius=25&sort=<required>&st=<required>&start=<required>&useragent=<required>&userip=<required>&v=2",
                       headers={
    "X-Mashape-Key": "5DB85U4ShnmshrsLnWmemYWZUsWFp1ZuxGVjsnD3lhI6oFWhiP",
    "Accept": "application/json"
  })
