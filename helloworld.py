import numpy as np
import cv2 
from numpy.core._internal import _commastring

img = cv2.imread("timg.jpg",0)
#print img
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#print img
px = img
#print px
print px.shape #(hight, length)
np.savetxt("foo.txt", img , fmt= '%i')
print type(img)
#scale = np.zeros((480,720))
scale = cv2.resize(img, (600, 400))
scaleWidth = 600
scaleHeight = 400
cv2.imshow('image',scale)
cv2.waitKey( )
cv2.destroyAllWindows() 


def Gkernel(kernelSize, sigma):
    kernel = np.zeros((kernelSize,kernelSize))
    for i in range(0,kernelSize):
        for j in range(0,kernelSize):
            centre = (kernelSize -1 )/2
            kernel[i,j] =  kernel[i,j]=np.exp(-((i-centre)**2+(j-centre)**2)/(2*sigma**2))
    kernelSum = np.sum(kernel)
    
    return kernel, kernelSum

def iKernel(kernelSize):
    kernel = np.zeros((kernelSize,kernelSize))
    center = (kernelSize -1)/2
    kernel[center,center] = 1
    return kernel, 1 











































#apply filter to the image for simulated residual vision.
print type(scale)
print scale.shape
mask = np.zeros((400,600))
'''
a = np.zeros((2,2))
a[0,0] = 1 
a[0,1] = 2
b = np.zeros((1,2))
print b
'''
maskOriginX = 299 
maskOriginY = 199
maskRadus = 22
Rsquare = maskRadus**2 

for x in range(maskOriginX - maskRadus , maskOriginX + maskRadus) :
    for y in range(maskOriginY- maskRadus, maskOriginY + maskRadus) :
       if ( (x-maskOriginX)**2 + (y-maskOriginY)**2 ) < Rsquare :
           mask[y,x]  = 1 
        
            
            
masked = np.copy(scale)          
            
for i in range(0, scaleHeight):
    for j in range (0, scaleWidth):
        if mask[i,j] == 0 :
           masked[i,j] = 0
           
cv2.imshow('masked', masked)
cv2.waitKey( )
cv2.destroyAllWindows()
#guassin filtering
#gnerating kernel; 
#Phosphene seperation: 3 degrees = 3 *4.4 = 13.2 px sagma is 13.2*0.66 = 8.712
#generation of gaussain keneral

kernel = np.zeros((19,19))
sigma = 8.712      
for i in range(0,19):
 
    for j in range(0,19):
       kernel[i,j] =    np.exp(  - ((i-9)**2 + (j-9)**2) / (2*sigma**2))
#print (kernel)
kernelSum = np.sum(kernel)
print kernelSum 

# finding the position of phosphenes
############################MMMMMMMMMMMIIIIIIISSSSSSSSSSSTTTTTTTAAAAAAAAAAKKKKKKKKKEEEEEE HHHHHHHHEEEEEEERRRRRRRREEEEEEEEEEEEE
visionField10 = np.zeros((10,10,2))
visionField10[0,0,0] = 143 
visionField10[0,0,1] = 243
#print visionField10[0,0] 
for i in range(0,10):
    for j in range(0,10): 
        visionField10[i,j,0] = visionField10 [0,0,0] + i * 14
        visionField10[i,j,1] = visionField10 [0,0,1] + j * 14
#print visionField10[9,9,1] 

#clipping the scaled image
 

L = list()
for i in range(0 , 10):
    L.append([])

for i in range(0,10):
    for j in range(0,10):
        g = scale[visionField10[i,j,0]-9:visionField10[i,j,0]+10,visionField10[i,j,1]-9:visionField10[i,j,1]+10]
        L[i].append(g)


b = L[5][5]
a = cv2.resize(b, (600,400))
cv2.imshow('g', b)
cv2.waitKey( )
cv2.destroyAllWindows()
#Applying filter

average = np.zeros((10,10))

for i in range(0,10):
    for j in range(0,10):
        clip = np.copy(L[i][j])
        average[i,j] = np.sum(np.multiply(clip, kernel)) /kernelSum

e = average.astype('uint8')
#blur = cv2.GaussianBlur(scale,(15,15),0)
cv2.imshow('i',e )
print type(e[1,1])
cv2.waitKey( )
cv2.destroyAllWindows()
phos = np.zeros((400,600))
phos = phos.astype('uint8')
for i in range(0,10):
    for j in range(0,10):
        phos[visionField10[i,j,0]-3:visionField10[i,j,0]+4, visionField10[i,j,1]-3:visionField10[i,j,1]+4] = e[i,j]
cv2.imshow('h', phos) 
cv2.waitKey( )
cv2.destroyAllWindows()




'''
print type(kernel) 
print  np.shape(kernel)

c = np.zeros((10,10))
print type(L[1][1]) 
c = np.copy(L[1][1])
print  np.shape(c)
'''



