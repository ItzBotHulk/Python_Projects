import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

ironMan_image = face_recognition.load_image_file("fcData/ironMan.jpg")
ironMan_encoding = face_recognition.face_encodings(ironMan_image)[0]

thor_image = face_recognition.load_image_file("fcData/thor.jpg")
thor_encoding = face_recognition.face_encodings(thor_image)[0]

face_encodings = [ironMan_encoding, thor_encoding]
face_name = ["Iron Man", "Thor"]

student = face_name.copy()

face_location = []
face_encodings = []

now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(f"{current_date}.csv", "w+", newline="")
lnWriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    face_location = face_recognition.face_location(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_location)
    
    for face_encoding in face_encodings:
        mathes = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
    
    best_match_index = np.argmin(face_distance)

    if(matches[best_match_index]):
        name = known_face_names[best_match_index]
        
        if name in face_name:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255,0,0)
            thickness = 3
            lineType = 2
            cv2.putText(frame,name + " Presente ", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in student:
                student.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnWriter.writerow([name, current_time])
        
        cv2.imshow("Attendace",frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
        video_capture.release()
        cv2.destroyAllWindows()
        f.close()