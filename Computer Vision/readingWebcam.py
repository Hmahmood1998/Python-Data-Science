import cv2

# img=cv2.imread('images.jpg')
# print(img)

# cv2.imshow('my window',img)

# cv2.waitKey(5000)

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('my webcam',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

    

cv2.destroyAllWindows()
cap.release()
