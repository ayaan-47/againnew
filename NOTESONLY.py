NOTES FOR PYTHON CV 


TEMPLATE MATCHING NOTES


##Template Matching
## MATCHING TWO PICTURES USING TEMPLATE MATCHING METHODS 

## ABOVE MENTIONED ARE THE METHODS GIVEN TO USE IT



import cv2
import numpy as np
import matplotlib.pyplot as plt

full = cv2.imread('Test.jpg')
full = cv2.cvtColor(full,cv2.COLOR_BGR2RGB)


face=cv2.imread('Test2.jpg')
face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for m in methods:
    #CREATING A COPY
    full_copy = full.copy()
    method = eval(m)

    # Template MAtching

    res = cv2.matchTemplate(full_copy,face,method)



my_method = eval('cv2.TM_CCOEFF')
res = cv2.matchTemplate(full,face,my_method)

plt.imshow(res)
plt.show()