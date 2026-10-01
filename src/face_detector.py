import cv2

class FaceDetector:
    def __init__(self):
        self.face = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.eye = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye.xml"
        )

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return self.face.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(100,100)
        )

    def detect_eyes(self, frame, face):
        x, y, w, h = face
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        roi = gray[y:y+h, x:x+w]
        eyes = self.eye.detectMultiScale(
            roi, scaleFactor=1.1, minNeighbors=7, minSize=(20,20)
        )
        return len(eyes), eyes
