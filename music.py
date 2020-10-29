# Plays music from using the Spotify API

import requests
from config import api_token, refresh_token
from refresh import refresh
import time

class Player(object):
    '''
    Class to represent a Spotify music controls.

    Attributes:
        spotify_token (str): Spotify API token with user-modify-playback-state allowed in the scope
        device_id (str): Device ID of the device used to play music
        music_playing (bool): Flag of whether music is currently playing
        header (dict): Header needed for requests
    '''
    
    def __init__(self):
        '''
        Constructor for the Player class, calls the call_refresh once instantiated to generate an updated API token.
        '''
        self.spotify_token = ''
        self.device_id = ''
        self.music_playing = False

        # Run call_refresh to generate working API token
        self.call_refresh()
        self.header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.spotify_token}'
        }

    def start_music(self):
        '''
        Starts music from where the user last left off via PUT request.
        '''
        self.call_refresh()
        self.device()

        query = f'https://api.spotify.com/v1/me/player/play?device_id={self.device_id}'
        response = requests.put(query, headers=self.header)
        
        if response.ok:
            self.music_playing = True

    def pause_music(self):
        '''
        Pauses music from where the user last left off via PUT request.
        '''
        self.call_refresh()
        self.device()

        query = f'https://api.spotify.com/v1/me/player/pause?device_id={self.device_id}'
        response = requests.put(query, headers=self.header)

        if response.ok:
            self.music_playing = False
  
    def device(self):
        '''
        Retreives device ID via a GET request
        '''
        self.call_refresh()

        query = 'https://api.spotify.com/v1/me/player/devices'
        
        header = {
            'Authorization': f'Bearer {self.spotify_token}'
        }
        
        response = requests.get(query, headers=header)
        response_json = response.json()
        self.device_id = response_json['devices'][0]['id']
    

    def call_refresh(self):
        '''
        Creates an instance of the Refresh class, which uses Spotify's refresh token to generate a new API token.
        '''

        self.spotify_token = refresh()


if __name__ == '__main__':
    songs = Player()
    songs.device()
    songs.start_music()
    time.sleep(5)
    songs.pause_music()

