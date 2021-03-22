import cv2
import sys
import numpy as np 


img=cv2.imread(sys.argv[1],cv2.IMREAD_UNCHANGED)
scale_percent=95 #percent to scale

width_and_height=int(img.shape[0]*scale_percent/100)
dim=(width_and_height,width_and_height)

#resize
img=cv2.resize(img,dim, interpolation = cv2.INTER_AREA)


#make a template for mask and input image
mask_template=np.array([[255,255,255] for i in range(256*256)]).reshape(256,256,3)

start=int(256/2-width_and_height//2)
end=start+width_and_height
image,mask=mask_template.copy(),mask_template.copy()

image[start:end,start:end,:]=img
mask[start:end,start:end,:]=[0,0,0]


cv2.imwrite("soruce/esher.jpg",image)
cv2.imwrite("mask/mask.jpg",mask)
