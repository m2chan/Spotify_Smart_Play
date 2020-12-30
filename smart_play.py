# Main script that runs the program
# Must run from command line!

from detect_user import MotionDetector
from music import Player
import cv2
from threading import Thread
import time


class SmartPlay(object):
    def __init__(self):
        
        # Instantiate objects
        self.detector = MotionDetector()
        self.music_controls = Player()

        # Start video capture and initialize frames and variables
        self.capture = cv2.VideoCapture(0)

        self.capture.set(3, 640)
        self.capture.set(4, 480)

        self.ret1, self.frame1 = self.capture.read()
        self.ret2, self.frame2 = self.capture.read()

        self.thresh = self.frame1

        self.static_frame_counter = 0
        self.music_controls.start_music()

        self.room_status = 'Occupied'
        self.music_status = 'Playing'

        self.frame_count = 0
        self.start_time = time.time()

        # Set up thread for polling
        self.thread = Thread(target=self.poll, args=())
        self.thread.daemon = True
        self.thread.start()


    def poll(self):
        '''
        Polls new frames from the webcam in a separate thread. Updates instance variables with newly polled frame for use in analysis and output.
        '''
        
        while True:
            self.ret2, self.frame2 = self.capture.read()
                
    
    def analyze(self):
        '''
        Analyze frames for motion, and adjust Spotify stream accordingly. Runs on main thread.
        '''
        self.frame1, self.thresh = self.detector.detect_motion(self.frame1, self.frame2, self.room_status, self.music_status)
        self.frame_show = self.frame1
        self.frame1 = self.frame2
        self.frame_count += 1

        # If the user is in the room, then start playing music if music was stopped
        if self.detector.user_in_room:
            self.static_frame_counter = 0
            if not self.music_controls.music_playing:
                self.music_controls.start_music()

            self.room_status = 'Occupied'
            self.music_status = 'Playing'

        # Music keeps playing if there is no more motion detected for up to ~2 seconds
        # In case user quickly walks off or stands/sits very still
        elif not self.detector.user_in_room and self.static_frame_counter < 30:
            self.static_frame_counter += 1
            self.room_status = 'Empty'
            self.music_status = 'Playing'
        
        # If no movement detected for >2 seconds, then pause music
        else:
            if self.music_controls.music_playing:
                self.music_controls.pause_music()

            self.room_status = 'Empty'
            self.music_status = 'Paused'

    def show_frame(self):
        '''
        Outputs windows for motion detection and diffs. Runs on main thread.
        '''

        cv2.imshow('Motion Detection', self.frame_show)
        cv2.imshow('Differences', self.thresh)

        # Escapes with ESC key
        if cv2.waitKey(40) == 27:
            self.stop()
    
    def stop(self):
        '''
        Close windows, stop video capture, and pause music
        '''
        self.capture.release()
        cv2.destroyAllWindows()
        self.music_controls.pause_music()
        print('FPS: ', self.frame_count/(time.time() - self.start_time))
        exit(1)

def main():
    smart_play = SmartPlay()
    while True:
        smart_play.analyze()
        smart_play.show_frame()

if __name__ == '__main__':
    main()
    