# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:33:18 2018

@author: puter
"""

import os

print(os.listdir("../wk5"))
print("--------")

for d in os.scandir():
    print(d.name)
    print(d.path)
    print(d.inode())
    print(d.is_dir)
    print(type(d))
    
