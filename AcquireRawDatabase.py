# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:25:50 2017

@author: pascal
"""

# -*- coding: utf-8 -*-
import serial
import time
import pickle
#import numpy
from ESP8266_functions import acquire

#path = './data15.txt'
#f1 = open(path,'w')
#s.close()
 
ser = serial.Serial(2)  # open first serial port
print(ser.portstr)       # check which port was really used
ser.timeout=.1
ser.baudrate=115200

num_acqu=200
position='Bureau_moving'

all_acqu=[]
for i in range(num_acqu):
  print("Acquisition "+str(i+1)+" of "+str(num_acqu))
  one_acqu=acquire(ser)
  all_acqu.append(one_acqu)
  if all_acqu[-1]==[]:
      print('No WiFi Detected')
  
ser.close()

with open(position+str(num_acqu)+".txt", "wb") as fp:   #Pickling
   pickle.dump(all_acqu, fp)
