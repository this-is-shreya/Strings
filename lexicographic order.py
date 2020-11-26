# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:09:25 2020

@author: shrey
"""

a=input().split(",")#taking addresses as input splitted by comma
l=[]
count=0
temp=0
b=0
l.append(a[0])#appending the first element in a to l
for i in range(len(a)):
    for j in range(len(l)):
        if a[i]>l[j]:
            
            count=count+1
            
            
        if a[i]<l[j]:
            
            temp=temp-1  
            b=j
            
            
    if count>0 and temp==0:
        l.append(a[i])#if a number is greater than all elements in the list, 
        #append it at the last
        count=0
    if count==0 and temp<0:
        l.insert(0,a[i])#if a number is smaller than all elements in the list, insert it at
        #the first position
        temp=0
    if count>0 and temp<0:
        l.insert(b,a[i])#if a number is less than and greater than particular values
        #then add it to the list before the number it is lesser than
        b=0
        count=0
        temp=0
        
        
print(l)
