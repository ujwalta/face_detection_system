import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier('haarcascade_frontal_face_default.xml')

webcam = cv2.VideoCapture(0)

while True:
    ret, img = webcam.read()
    if not ret:
        break

    # ✅ FLIP CAMERA (mirror fix)
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_roi = img[y:y+h, x:x+w]

        try:
            result = DeepFace.analyze(
                face_roi,
                actions=['emotion'],
                enforce_detection=False
            )
            emotion = result[0]['dominant_emotion']
        except:
            emotion = "Detecting..."

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(
            img,
            emotion,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face & Emotion Detection", img)

    if cv2.waitKey(10) & 0xFF == 27:
        break

webcam.release()
cv2.destroyAllWindows()

