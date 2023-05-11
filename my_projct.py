import cv2
import vonage
from playsound import playsound
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame,1.2,5)
    for (x,y,w,h) in fire:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h , x:x+w]
        print('Fire is detected')
        playsound('audio.mp3')
        client = vonage.Client(
            application_id="de3e2f19-596d-4154-9811-8815224c41dd",
            private_key="private.key",
        )

        voice = vonage.Voice(client)

        response = voice.create_call({
            'to': [{'type': 'phone', 'number': "966550724999"}],
            'from': {'type': 'phone', 'number': "966550724999"},
            'ncco': [{'action': 'talk', 'text': 'worrng alestraha naaaar'}]
        })

    cv2.imshow('Hani', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break