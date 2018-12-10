import numpy as np 
import cv2 
import random
t1 = np.zeros((19,19))
t1 = t1.astype('uint8')


x1 = (3,3)
x2 = (3,5)
x3 = (7,7)
x4 = (8,8)
x5 = (10,10)
x6 = (11,11)
x7 = (13,13)
x8 = (15,15)
x9 = (17,17)

y1 = (10,1)
y2 = (10,4)
y3 = (10,6)

y4 = (10,13)
y5 = (10,15)
y6 = (10,19)

z1 = (17,17)
z2 = (15,15) 
z3 = (13,13)
z4 = (11,11) 
z5 = (9,9)
z6 = (7,7) 
z7 = (5,5)
z8 = (3,3)


h1 = (19,10) 
h2 = (17,10) 
h3 = (15,10)
h4 = (13,10)
h5 = (7,10) 
h6 = (5,10)
h7 = (3,10)
h8 = (1,10)

xn1 = (0,0)
xn2 = (0,0) 
yn1 = (0,0)
yn2 = (0,0)
zn1 = (0,0)
zn2 = (0,0)
hn1 = (0,0)
hn2 = (0,0) 

def ranShape():
#x axis section 1 
    i = random.randint(1,5)
    if i == 1:
        xn1 = x1  
    if i == 2: 
        xn1 = x2
    if i == 3:
        xn1 = x3
    if i == 4:
        xn1 = x4 
    if i == 5:
        xn1 = x5 
    if i == 6:
        xn1 = x6  
    if i == 7: 
        xn1 = x7
    if i == 8:
        xn1 = x8
    if i == 9:
        xn1 = x9 

    # x axis section 2
    j = random.randint(6,9)
    if j == 1:
        xn2 = x1  
    if j == 2: 
        xn2 = x2 
    if j == 3:
        xn2 = x3
    if j == 4:
        xn2 = x4 
    if j == 5:
        xn2 = x5 
    if j == 6: 
        xn2 = x6
    if j == 7:
        xn2 = x7 
    if j == 8: 
        xn2 = x8
    if j == 9: 
        xn2 = x9
#y axis section 1
    i = random.randint(1,3)
    if i == 1:
        yn1 = y1  
    if i == 2: 
        yn1 = y2 
    if i == 3:
        yn1 = y3
    if i == 4:
        yn1 = y4 
    if i == 5:
        yn1 = y5 
    if i == 6: 
        yn1 = y6
# y axis section 2
    j = random.randint(4,6)
    if j == 1:
        yn2 = y1
    if j == 2:
        yn2 = y2
    if j == 3:
        yn2 = y3
    if j == 4:
        yn2 = y4 
    if j == 5:
        yn2 = y5 
    if j == 6:
        yn2 = y6
#z axis section 1
    i = random.randint(1,4)
    if i == 1:
        zn1 = z1
    if i == 2:
        zn1 = z2
    if i == 3:
        zn1 = z3
    if i == 4:
        zn1 = z4 
    if i == 5:
        zn1 = z5 
    if i == 6:
        zn1 = z6
    if i == 7:
        zn1 = z7
    if i == 8:
        zn1 = z8
#z axis section 2
    j = random.randint(5,8)
    if j == 1:
        zn2 = z1  
    if j == 2: 
        zn2 = z2 
    if j == 3:
        zn2 = z3
    if j == 4:
        zn2 = z4 
    if j == 5:
        zn2 = z5 
    if j == 6: 
        zn2 = z6
    if j == 7: 
        zn2 = z7
    if j == 8: 
        zn2 = z8
#h axis section 1
    i = random.randint(1,4)
    if i == 1:
        hn1 = h1  
    if i == 2: 
        hn1 = h2 
    if i == 3:
        hn1 = h3
    if i == 4:
        hn1 = h4 
    if i == 5:
        hn1 = h5 
    if i == 6: 
        hn1 = h6
    if i == 7: 
        hn1 = h7 
    if i == 8: 
        hn1 = h8 
#h axis section 2
    j = random.randint(5,8)
    if j == 1:
        hn2 = h1  
    if j == 2: 
        hn2 = h2 
    if j == 3:
        hn2 = h3
    if j == 4:
        hn2 = h4 
    if j == 5:
        hn2 = h5 
    if j == 6: 
        hn2 = h6
    if j == 7: 
        hn2 = h7 
    if j == 8: 
        hn2 = h8
    return xn1,yn1,zn1,hn1,xn2,yn2,zn2,hn2

xn1,yn1,zn1,hn1,xn2,yn2,zn2,hn2 = ranShape()
t8 = np.zeros((19,19))
t8 = t8.astype('uint8')
myROI = [xn1,yn1,zn1,hn1,xn2,yn2,zn2,hn2]
cv2.fillPoly(t8, [np.array(myROI)], 255) 
t2 = np.zeros((600,400))
t9 = t2.astype('uint8')
t9 = cv2.resize(t9,(600,400))

#get coordinate 
numberOfPhos = 20
sigma = 8.712
phosSep = 17
kernelSize = 19
phoSize = 17


visionField = np.zeros((numberOfPhos, numberOfPhos, 2))
leftTopCornerR = 199-((numberOfPhos/2)-1) * phosSep
leftTopCornerC = 299-((numberOfPhos/2)-1) * phosSep
visionField[0,0,0] = leftTopCornerR
visionField[0,0,1] = leftTopCornerC
for i in range (0,numberOfPhos):
    for j in range(0,numberOfPhos): 
        visionField[i,j,0] = visionField[0,0,0] + i * phosSep
        visionField[i,j,1] = visionField[0,0,1] + j * phosSep



c = 255 #haven't used, pay attention!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(0,numberOfPhos):
    for j in range(0,numberOfPhos):
        c = c - 1
        xn1,yn1,zn1,hn1,xn2,yn2,zn2,hn2 = ranShape()
        t8 = np.zeros((19,19))
        t8 = t8.astype('uint8')
        myROI = [xn1,yn1,zn1,hn1,xn2,yn2,zn2,hn2]
        
        cv2.fillPoly(t8, [np.array(myROI)], 255)
        t10 = cv2.resize(t8,(phoSize,phoSize))
        shift1 = random.randint(-10,10)
        shift2 = random.randint(-10,10)
        h = visionField[i,j,0] + shift1#position shift
        g = visionField[i,j,1] + shift2
       
        
        #something other than i and j should be used other wise there will be only one column and one raw.
        for z in range(0,phoSize-1):
            for p in range(0,phoSize-1):
                a = t9[z+h,p+g]
                a = a.astype('double')
                if a == 0:
                    t9[z+h, p+g] = t10[z,p]
                #t9[z+h,p+g] = t10[z,p]
        #for q in range(0,phoSize+1):
        #    for w in range(0,phoSize+1):
        #        if t9[q+h,w+g] == 255 : 
        #            t9[q+h,w+g] = c 
                    

                
#np.savetxt("fool.txt",t9 , fmt= '%i')
            
            
    
while (True):
        cv2.imshow("x",t9)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
#cv2.imshow("x", t9)
#w hile (True):
#    cv2.imshow('y',t8)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

