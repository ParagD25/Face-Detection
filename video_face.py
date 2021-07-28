import cv2

face_file=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_capture=cv2.VideoCapture(0)

while True:
    check,frame=face_capture.read()
    gray_scale_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_file.detectMultiScale(gray_scale_img,scaleFactor=1.05,minNeighbors=4)

    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Face Capturing',img)
    press_key=cv2.waitKey(1)
    if press_key==ord('q'):
        break
    
face_capture.release()
cv2.destroyAllWindows()
