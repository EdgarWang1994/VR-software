'''
Created on 2 Jan. 2019

@author: Edgar
'''
import numpy as np 
import cv2 


t1 = np.zeros((600,400))
t1 = t1.astype('uint8')

t1 = cv2.resize(t1,(600,400))



xfile=open('xf.txt','r')
yfile=open('yf.txt','r')
xlines=xfile.readlines()
ylines=yfile.readlines()
#remove the space in the array read from file
#x = lines[0].split()
#print x 
#y = map(int,x)
#print y

LoL =(len(xlines))
maskListLen = LoL
print LoL
XmaskList = list()
YmaskList = list()
for i in range(0,LoL):
    XmaskList.append(map(int,xlines[i].split()))
    YmaskList.append(map(int,ylines[i].split()))
    #print maskList[i-1]
for i in range(0,LoL):
    xline = np.copy(XmaskList[i])
    yline = np.copy(YmaskList[i])
    for j in range(0, xline.size):
        t1[xline[j]][yline[j]] = i


while (True):
        cv2.imshow("x",t1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break