import cv2
img = cv2.imread("Container.jpg", cv2.IMREAD_GRAYSCALE)
ret,threst1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) 
cv2.imshow("Input image", img)
cv2.imshow("Processed image", threst1)
cv2.waitKey(50000)
cv2.destroyAllWindows()