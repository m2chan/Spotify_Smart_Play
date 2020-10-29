# Automatic_Music

## About the Project

I usually play music or podcasts out loud using Spotify on my computer while I work, but a pain point is needing to pause the content I'm listening to when I walk away from my desk. Trying to pause Spotify involves digging for the tab that I opened the Web Player on, of if I'm listening to using the desktop app, finding and opening that.

Automatic Music is a tool that uses motion detection and object tracking with my computer's webcam (also works on any other video input) to determine if I'm still around. If I am, then my content will continue to play, but if I walk away to outside of the frame of the video, then my Spotify stream will get paused, and only resume when it detects that I'm back. Rather than me telling you, here's a live demo:

[Insert video]

Some other notes on functionality:
* Content is paused once I leave the frame for ~2 seconds or more, so that if I just want to grab something quickly, my stream isn't interrupted.
* This runs seamlessly on top of Spotify, so users can freely change tracks, playlists, etc. on Spotify and even the devices that they're listening on, without impacting the functionality of this tool.
* Object tracking rectangles are a visualization tool to illustrate more significant movements, but all movements (down to the pixel level) are being tracked to see if the user is still in the frame.

As I've integrated this tool into my day-to-day life, some interesting functionalities I hope to add are: 
* Gestures for media and volume controls
* Facial recognition for custom playlists for different people in the household

## Technical details

This project was build using Python. 

Tools:
* OpenCV for motion detection and object tracking
* Spotify API for music start/pause (must allow app access from personal account)
* Libraries: Requests, Numpy

#### Thanks for checking out my project! :wave:






