# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:06:15 2018

"""

import json

search_criteria={"fiscal_year":["2012","2013","2014","2015","2016","2017","2018"],
                 #"asset_type":["Playground","Bridge","Playing Field"]}
                 "asset_type":["Bridge","Playground","Facility"],
                 "status":["Planned"],
                 "area":["Engineering and Construction","Administration/Sub-Award"],
                 "start_date":[]
                 ## TO DO: start date
                 ## use datetime.date(yyyy,mm,dd) to process in searchIt.py
                 }


print(search_criteria.keys()) ##just so we can see some output when we create the JSON file

with open('cp_search_criteria.json','w') as outfile:
    json.dump(search_criteria,outfile)
    
""" 

    SNIPPETS AND NOTES AND SUCH:
     
    for AND vs OR:
        
    I kinda think it should be something like:
    {"fiscal_year":{"AND1":"2014","OR1":"2011","AND2":"2015"}}
    or maybe even ..."AND1":["2014","2018"], "OR1":["2010"]
    
"""

