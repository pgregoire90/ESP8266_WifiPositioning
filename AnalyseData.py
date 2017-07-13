# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:11:04 2017

@author: pascal
"""

import numpy as np
import matplotlib.pyplot as plt

d=[]
temp1=''

alldat=[]
for i in range(1,16):
    path = './data'+str(i)+'.txt'
    f1 = open(path,'r')
    q=f1.read()
    q=q.splitlines()
    wi=[]
    for x in q:
        t=x.split()
        #print(len(t))
        if len(t)>4:
            temp3=temp1.join(t[:-3])
            temp2=t[-3:]
            t=[]
            t.append(temp3)
            t.append(temp2[0])
            t.append(temp2[1])
            t.append(temp2[2])
            #print(t)           
        name=t[0].split('\"')
        force=float(t[1])
        std=float(t[2])
        nu=float(t[3])
        
        li=[name[1], force, std, nu]
        
        wi.append(li)
    alldat.append(wi)
    

namebase=[]
forcebase=np.zeros((15,25))-100
i=0
#first index 0:14 is the data,second index refers to the name of wifi
for dat in alldat:
    
    for wif in dat:
        if namebase.count(wif[0])==0:
            namebase.append(wif[0])
            forcebase[i,len(namebase)-1]=wif[1]
        else:
            j=namebase.index(wif[0])
            forcebase[i,j]=(wif[1])
    i=i+1
    
for i in range(2,3):
    ha_p=plt.plot(forcebase[:,i],'o-', label=str(i))
plt.show()