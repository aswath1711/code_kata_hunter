# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:34:22 2019

@author: New
"""

a,b=map(int,input().split())
li1=list(map(int,input().split()))[:a]
li2=list(map(int,input().split()))[:b]
res=[]
for i in range(len(li1)):
        for j in range(len(li2)):
                if(li1[i]==li2[j]):
                        res.append(li2[j])
res.sort()
li2.sort()
if(res==li2):
        print("YES")
else:
        print("NO")