import cv2
import numpy
import scipy


img = cv2.imread("D:/py/tryml.png")



img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow("image",img)
#cv2.waitKey(0)

#cv2.imshow("Gray",img2)
#cv2.waitKey(0)

_, img3 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
#cv2.imshow("binary",img3)
#cv2.waitKey(0)
print("hi")
print(img3)

row = img3.shape[0]
col = img3.shape[1]

height=0
width=0
for j in range(col):
     
    for i in range(row):
        if img3[i][j] != 0:
            width=width+1
            break

print("Width is: ", width)

for i in range(row):
     
    for j in range(col):
        if img3[i][j] != 0:
            height=height+1
            break
        
print("Height is: ",height)

            
    


cv2.destroyAllWindows()