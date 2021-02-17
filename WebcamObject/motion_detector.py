import cv2,time
video = cv2.VideoCapture(0)
first_frame=None
while True:
    check, frame = video.read()

    #time.sleep(3)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray= cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)

    cv2.imshow("capturing", frame)
    cv2.imshow("delata frame", delta_frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()