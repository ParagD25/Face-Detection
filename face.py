import cv2
face_file=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("Images/img4.png")
gray_scale_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_file.detectMultiScale(gray_scale_img,scaleFactor=1.05,minNeighbors=4)

for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Face Detect',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
