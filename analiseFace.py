import cv2
from cvzone.FaceDetectionModule from FaceDetector

video = cv2.VideoCapture(0)

detector = FaceDetector

while True:
    _,img = true.read()
    img, bboxes = detector.FindFace(img =, draw=True)

    cv2.imshow('Reconhecimento de face', img)
    if cv2.waitKey(1) == 27:
        break 