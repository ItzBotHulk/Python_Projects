import cv2
import numpy as np

def compare_video_gestures(vide1_path, vide2_path, threshold=0.9):
#capture the videos
    cap1 = cv2.VideoCapture(vide1_path)
    cap2 = cv2.VideoCapture(vide2_path)

    #checking if videos are opening or not
    if not (cap1.isOpened() and cap2.isOpened()):
        print("Error: Unable to open videos.")
        return

    #it read the first frame from video1. 
    ret1, frame1 = cap1.read()
    if not ret1:
        print("Error: Unable to read the first frame from video1.")
        return

    #it read the first frame from video2
    ret2, frame2 = cap2.read()
    if not ret2:
        print("Error: Unable to read the first frame from video2.")
        return

    #convertint the template gesture to grayscale
    gesture_template_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    #size of the template gesture
    template_height, template_width = gesture_template_gray.shape[:2]

    #green color for the text
    green = (0, 255, 0)  

    #loop for frames of video1
    while True:
        #convert frame1 to grayscale
        frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

        #resize frame1_gray to match the size of gesture_template_gray
        frame1_gray_resized = cv2.resize(frame1_gray, (template_width, template_height))

        #template matching.
        res = cv2.matchTemplate(frame1_gray_resized, gesture_template_gray, cv2.TM_CCOEFF_NORMED)

        #max correlation
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        #checking if gesture is detected or not .
        if max_val >= threshold:
            print("Gesture Detected!")
            #it write gesture detected in top right corner.
            cv2.putText(frame1, "Gesture Detected!", (frame1.shape[1] - 300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 2, cv2.LINE_AA)

        #display frame1 with detected results.
        cv2.imshow("Video 1", frame1)


        #it read next frame
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        #loop will break if video is ended.
        if not ret1 or not ret2:
            break
        
        #if we type q we will exit from the code/display screen.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    #closing video files.
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()
    
#video here -->
#Use same videos to check gesture is same from first video or not ;
video1_path = "test_2.mp4"
video2_path = "test_2.mp4"
compare_video_gestures(video1_path, video2_path)
