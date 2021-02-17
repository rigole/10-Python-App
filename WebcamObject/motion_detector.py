import cv2,time
video = cv2.VideoCapture(0)
first_name=None
while True:
    check, frame = video.read()

    #time.sleep(3)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if first_name is None:
        first_name=gray
        continue

    cv2.imshow("capturing", frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()