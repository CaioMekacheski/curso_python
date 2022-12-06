import cv2


webcam = cv2.VideoCapture(0)
frame_w = int(webcam.get(3))
frame_h = int(webcam.get(4))
size = (frame_w, frame_h)
result = cv2.VideoWriter('teste.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
if webcam.isOpened():
    validation, frame = webcam.read()

    while validation:
        validation, frame = webcam.read()
        cv2.imshow('teste webcam', frame)
        result.write(frame)
        key = cv2.waitKey(5)


        if key == 27:
            break
    cv2.imwrite('teste.png', frame)


webcam.release()
cv2.destroyAllWindows()