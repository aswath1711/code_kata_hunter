# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:53:48 2019

@author: New
"""

n=int(input())
l=list(map(int,input().split()))
r=1
l1=[]
for i in l:
  r=r*i
for i in l:
  l1.append(r//i)
print(*l1)
