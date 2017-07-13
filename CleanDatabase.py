# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:17:04 2017

@author: pascal
"""

import pickle
import random

files=['Bureau_moving200.txt','Salon_moving200.txt','Cuisine_moving200.txt']
targets=['Bureau','Salon','Cuisine']

databasename="ESP8266_database_moving1"

dic={}
for file in files:
  with open(file, "rb") as fp:   # Unpickling
    acquisitions = pickle.load(fp)
    for acquisition in acquisitions:
        for wifi in acquisition:
            if dic.get(wifi[0]):
                dic[wifi[0]]=dic[wifi[0]]+1
            else:
                dic[wifi[0]]=1

#print(dic)
sorted_list=sorted(dic.keys(),key=dic.__getitem__,reverse=True)
sorted_list_number=sorted(dic.values(),reverse=True)

#Remove if occurance is less than 5% of the time
clean_list=[]
for s,n in zip(sorted_list,sorted_list_number):
    
    if sorted_list_number[0]//20>n:
        print(str(s)+" Removed")  
    else:
        clean_list.append(s)
        
# Now we have a fixed list of wifi

data=[]
associated_target=[]
for file,target in zip(files,targets):
  with open(file, "rb") as fp:   # Unpickling
    acquisitions = pickle.load(fp)
    for acquisition in acquisitions:
        clean_acquisition=[-100]*len(clean_list)
        for wifi in acquisition:
            if wifi[0] in clean_list: # if wifi is in our list
                clean_acquisition[clean_list.index(wifi[0])]=wifi[1]
        data.append(clean_acquisition)
        associated_target.append(target)

# randomise order
q=list(zip(associated_target,data))
random.shuffle(q)
associated_target,data=zip(*q)

        
with open(databasename+".txt","wb") as fd:
    pickle.dump(data,fd)
    pickle.dump(associated_target,fd)

with open("cleanlist1.txt","wb") as fe:
    pickle.dump(clean_list,fe)

#to load that:    
#with open("ESP8266_database1.txt", "rb") as fp:   # Unpickling
#  q = pickle.load(fp)
#  w = pickle.load(fp)