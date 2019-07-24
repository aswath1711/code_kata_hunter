# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:45:20 2019

@author: New
"""

n=int(input())
l=list(map(int,input().split()))
a=[]
c=1
for i in range(n):
    for j in range(i,n):
        c=c*l[j]
        a.append(c)
    c=1
print(max(a))