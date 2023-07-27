import cv2
import numpy as np
img = cv2.imread('lena.jpg',1)
#img=np.zeros([512,512,3],np.uint0)
img=cv2.line(img,(0,0),(255,255),(0,255,0),6)
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),6)
img=cv2.rectangle(img,(385,0),(284,285),(255,0,0),5)
img=cv2.circle(img,(380,29),255,(0,255,0),6)
font =cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'hey nancee',(10,55),font,2,(245,55,256),cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()