# Main script that runs the program

from detect_user import MotionDetector
from music import Player
import cv2

def main():
    detector = MotionDetector()
    music_controls = Player()

    capture = cv2.VideoCapture(0)
    capture.set(3, 640)
    capture.set(4, 480)

    ret, frame1 = capture.read()
    ret, frame2 = capture.read()
            
    static_frame_counter = 0
    music_controls.start_music()

    room_status = 'Occupied'
    music_status = 'Playing'

    while True:
        frame1 = detector.detect_motion(frame1, frame2, room_status, music_status)
        cv2.imshow('Motion Detection', frame1)
        frame1 = frame2
        ret, frame2 = capture.read()
        
        if detector.user_in_room:
            static_frame_counter = 0
            if not music_controls.music_playing:
                music_controls.start_music()

            room_status = 'Occupied'
            music_status = 'Playing'

        elif not detector.user_in_room and static_frame_counter < 50:
            static_frame_counter += 1
            room_status = 'Empty'
            music_status = 'Playing'

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
