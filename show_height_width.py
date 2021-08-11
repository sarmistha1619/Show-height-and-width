import cv2

cap = cv2.VideoCapture('VideoFromCamera.mp4')

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()