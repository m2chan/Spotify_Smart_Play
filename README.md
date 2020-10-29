# Spotify_Smart_Play

## About the Project

I usually play music or podcasts out loud using Spotify on my computer while I work, but a pain point is walking away from my desk without pausing my stream and missing the best part of a song or an important detail in the podcast. Trying to pause Spotify in order to avoid this involves either digging for the tab that I opened the Web Player on, of if I'm listening to using the desktop app, finding and opening that. 

Spotify Smart Play is a tool that uses motion detection and object tracking with my computer's webcam (also works on any other video input) to determine if I'm still around. If I am, then my Spotify stream will start playing/continue to play, but if I leave the frame of the video, then my stream will get paused. My stream only resumes (picks up where it left off) when it detects that I'm back in the frame of the video. Here are some GIFSs on how it works, and a link to a YouTube video where you can hear the stream play and pause.

### Walking out of the room

Notice the status bars at the bottom of the left screen. It keeps track of whether the room is currently occupied or empty, and if the room is empty for ~2 seconds, the Spotify stream gets paused.

![walking out](https://media.giphy.com/media/cfMaYXxGELCJv51c4b/giphy.gif)

### Walking back into the room

Detects that the room is now occupied again, and unpauses the stream.

![walking in](https://media.giphy.com/media/yhenlpPgTXHgP2Lsxw/giphy.gif)

### Standing still

It is difficult to stand still enough in a room to trigger the false negative event of pausing Spotify while the user is still in the room. Notice that even as I try to stand still the tracking screen on the right still lights up.

![standing still](https://media.giphy.com/media/oo5WjqUoveuyuzJRoR/giphy.gif)

Here is the full [YouTube](https://youtu.be/0nSf3PnAm9A) video with sound.

Some other notes on functionality:
* Content is paused once I leave the frame for ~2 seconds or more, so that if I just want to grab something quickly, my stream isn't interrupted.
* This runs seamlessly on top of Spotify, so users can freely change tracks, playlists, etc. on Spotify and even the devices that they're listening on, without impacting the functionality of this tool.
* Object tracking rectangles are a visualization tool to illustrate more significant movements, but all movements (down to the pixel level) are being tracked to see if the user is still in the frame.

As I've integrated this tool into my day-to-day life, some interesting functionalities I hope to add are: 
* Gestures for media and volume controls
* Facial recognition to play custom playlists for different people in the household

## Technical details

This project was built using Python, tools used:
* OpenCV for motion detection and object tracking
* Spotify API for music start/pause (must allow app access from personal account)
* Libraries: Requests, Numpy

## Setup

Things you'll need:
* Python 3
* OpenCV - download using `pip install opencv-python`
* A Spotify premium account
* A computer with a webcam

You'll need to create a developer account on Spotify and create a new app, instructions and creation can be found [here](https://developer.spotify.com/dashboard/). Once you have created a new app in Spotify, follow the [Authorization Code Flow](https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow) to authenticate this app with your Spotify account. Make sure the Authorization Scope includes "user-modify-playback-state".

Once this is done, store your `client_id`, `client_secret`, `base_64_id` (64 bit encoded client_id and client_secret keys), `api_token`, and `refresh_token` in a `config.py` file in the same directory.

Once the `config.py` is set up, simply run `smart_play.py` to activate the tool. To exit, press the ESC key or right click on the Python window that opens up an select "Quit". 


#### Thanks for checking out my project! :wave:










