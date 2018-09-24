# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:29:42 2018


"""

numRows=100
countDownFrom = 1000
file2=open('challengeFile.txt','w')

for y in list(range(0,numRows)):
    for x in list(range(0,countDownFrom)):
        file2.write(str(x))
    countDownFrom -= countDownFrom
    file2.write('\n')

file2.flush()
file2.close()
