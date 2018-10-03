# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:13:59 2018

"""

import json

## specify upper $$threshold:percentage which applies to it
## enter "unlimited":percentage for unbounded upper tier

cost_schema={"10000":".08",
             "100000":".05",
             "unlimited":".5",
             "500000":".01"
             
        
        
        
        }

with open('cp_cost_schema.json','w') as outfile:
    json.dump(cost_schema,outfile)
