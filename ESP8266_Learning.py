# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn import datasets, svm, metrics
from mpl_toolkits.mplot3d import Axes3D

import serial
from ESP8266_Functions import acquire

com_port=6

print('Start')
with open("ESP8266_database_moving1.txt", "rb") as fp:   # Unpickling
  data = pickle.load(fp)
  target = pickle.load(fp)
data=np.array(data)
target=np.array(target)
#data = data.reshape(n_samples, -1)

n_samples=len(data)
# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.0007,kernel='rbf')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(10, 45)
ax.scatter([],[],[])


test_learn=0
if test_learn==1:   
    
  # We learn the digits on the first half of the digits
  classifier.fit(data[:n_samples // 2], target[:n_samples // 2])
  # Now predict the value of the digit on the second half:
  expected = target[n_samples // 2:]
  predicted = classifier.predict(data[n_samples // 2:])

  print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
  print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
else:
    classifier.fit(data[:n_samples], target[:n_samples])

    ### Now Aqcuire
    ser = serial.Serial(com_port-1)  # open first serial port
    print(ser.portstr)       # check which port was really used
    ser.timeout=.1
    ser.baudrate=115200
    
    with open("cleanlist1.txt","rb") as fe:
        clean_list=pickle.load(fe)
    
    for i in range(10):
      this_acqu=acquire(ser)
      this_clean_acquisition=[-100]*len(clean_list)
      for wifi in this_acqu:
        if wifi[0] in clean_list: # if wifi is in our list
          this_clean_acquisition[clean_list.index(wifi[0])]=wifi[1]
      this_data=np.array(this_clean_acquisition)
      this_data=this_data.reshape(1,-1)
      #print(this_data)
      this_prediction=classifier.predict(this_data)
      print(this_prediction) 
      x=this_clean_acquisition[0]
      y=this_clean_acquisition[1]
      z=this_clean_acquisition[2]
      ax.scatter(x,y,z,c='r', marker='o')
      ax.set_xlim([-100,-30])
      ax.set_ylim([-100,-30])
      ax.set_zlim([-100,-30])
      
      ax.scatter(x, -100, z,c='k', marker='o')
      ax.scatter(-100,y, z ,c='k', marker='o')
      ax.scatter(x, y, -100,c='k', marker='o')



      plt.draw()
      plt.pause(.01)
      #update_line(ax,this_clean_acquisition[:3])

ser.close()