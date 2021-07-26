import cv2
face_file=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("img2.jpg")

face=face_file.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('Face Detect',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
