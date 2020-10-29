# Main script that runs the program

from detect_user import MotionDetector
from music import Player
import cv2

def main():

    # Instantiate objects
    detector = MotionDetector()
    music_controls = Player()

    # Start video capture and initialize frames and variables
    capture = cv2.VideoCapture(0)
    capture.set(3, 640)
    capture.set(4, 480)

    ret, frame1 = capture.read()
    ret, frame2 = capture.read()
            
    static_frame_counter = 0
    music_controls.start_music()

    room_status = 'Occupied'
    music_status = 'Playing'

    # Loops until user hits ESC to exit the program
    while True:

        # Detect motion and output frame with text and motion tracking rectangle
        frame1 = detector.detect_motion(frame1, frame2, room_status, music_status)
        cv2.imshow('Motion Detection', frame1)
        frame1 = frame2
        ret, frame2 = capture.read()
        
        # If the user is in the room, then start playing music if music was stopped
        if detector.user_in_room:
            static_frame_counter = 0
            if not music_controls.music_playing:
                music_controls.start_music()

            room_status = 'Occupied'
            music_status = 'Playing'

        # Music keeps playing if there is no more motion detected for up to ~2 seconds
        # In case user quickly walks off or stands/sits very still
        elif not detector.user_in_room and static_frame_counter < 30:
            static_frame_counter += 1
            room_status = 'Empty'
            music_status = 'Playing'
        
        # If no movement detected for >2 seconds, then pause music
        else:
            if music_controls.music_playing:
                music_controls.pause_music()

            room_status = 'Empty'
            music_status = 'Paused'

        if cv2.waitKey(40) == 27:
            break

    cv2.destroyAllWindows()
    capture.release()
    music_controls.pause_music()

if __name__ == '__main__':
    main()
