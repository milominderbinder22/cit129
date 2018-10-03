# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:27:18 2018


"""

newFile=open('countdownPyramid.txt','w')

for i in range(10):
    for j in range(0,10-i):
        newFile.write(str(j))
    newFile.write("\n")
    newFile.flush()
newFile.close()
