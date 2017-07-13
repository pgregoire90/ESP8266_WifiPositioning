# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:05:02 2017

@author: pascal
"""

import time
import numpy
import matplotlib as plt

def acquire(ser):
  ser.write(b"AT+CWLAP\r\n")
  time.sleep(3)
    
  CWLAPline='Empty'
  one_acqu=[]
  while CWLAPline!=b'':
      CWLAPline=ser.readline()
      if CWLAPline[:6]==b"+CWLAP":
          wifiline=CWLAPline.split(b',')
          name=wifiline[1].split(b"\"")[1]
          force=int(wifiline[2])
          name_force=(name,force)
          one_acqu.append(name_force)
  return one_acqu;

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data[0]))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data[1]))
    hl.set_zdata(numpy.append(hl.get_zdata(), new_data[2]))
    plt.draw()