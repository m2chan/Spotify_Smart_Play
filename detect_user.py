# Detects when the user walks into the frame

import cv2

class MotionDetector(object):
    '''
    Class to represent an OpenCV motion detector.

    Attributes:
        user_in_room (bool): Flag to indicate whether the room is currently occupied or empty (based on whether or not there is motion)
    '''

    def __init__(self):
        '''
        Motion detector constructor.
        '''
        self.user_in_room = True
        
    def detect_motion(self, frame1, frame2, room_status, music_status):
        '''
        Detects motion by comparing the new frame with the previous frame.

        Parameters:
            frame1 (numpy.ndarray): Previous frame of video
            frame2 (numpy.ndarray): Current frame of video
            room_status (str): Status indicating whether room is empty or occupied
            music_status (str): Status indicating whether music is playing or paused
        '''

        # Get difference between 2 frames, convert to grayscale, and smooth differences to reduce noise
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Set threshold (determined via experimentation) to determine the difference, the dilate image to only focus on contours that are different
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through all the contours, and draw rectangle around contours that are larger than a certain size
        max_contour = 0
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            # If the contour is small, this is noise, so don't draw rectangle (determined via experimentation)
            if cv2.contourArea(contour) > 15000:
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            if cv2.contourArea(contour) > max_contour:
                max_contour = cv2.contourArea(contour)

        # Draw room and music status on the feed
        cv2.rectangle(frame1, (0, 430), (640, 480), (70, 61, 52), -1)
        cv2.putText(frame1, 'Room status: {}'.format(room_status), (62, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
        cv2.putText(frame1, 'Music status: {}'.format(music_status), (350, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        # If no contours with an area greater than 50 is present, then that indicates the room is empty, so adjust attribute
        if max_contour > 50: 
            self.user_in_room = True
        else: 
            self.user_in_room = False

        return frame1, thresh

if __name__ == '__main__':
    detect = MotionDetector()
    detect.start_camera_feed()
