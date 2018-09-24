# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:28:39 2018


"""

newFile=open('myFirstFile.txt','w')
hw="hello file world"
anInt=4
intAsStr=str(anInt)
newFile.write(intAsStr)
newFile.write(hw)
newFile.flush()
newFile.close()
