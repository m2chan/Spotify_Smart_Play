# Detects when the user walks into the frame

import cv2

class MotionDetector(object):
    def __init__(self):
        self.user_in_room = True
        
    def detect_motion(self, frame1, frame2, room_status, music_status):
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            # If the contour is small, this is noise, so don't draw rectangle
            if cv2.contourArea(contour) > 15000:
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.rectangle(frame1, (0, 430), (640, 480), (70, 61, 52), -1)
        cv2.putText(frame1, 'Room status: {}'.format(room_status), (70, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
        cv2.putText(frame1, 'Music status: {}'.format(music_status), (350, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        if contours: 
            self.user_in_room = True
        else: 
            self.user_in_room = False

        return frame1

if __name__ == '__main__':
    detect = MotionDetector()
    detect.start_camera_feed()
