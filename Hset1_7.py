# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:38:47 2019

@author: New
"""

n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(n):
    if i%2==0:
        if l[i]%2!=0:
            k.append(l[i])
    elif i%2!=0:
        if l[i]%2==0:
            k.append(l[i])
    else:
        pass
for i in range(len(k)-1):
    print(k[i],end=' ')
print(k[len(k)-1],end='')