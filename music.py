# Plays music from using the Spotify API

import requests
import urllib.parse
from config import api_token, refresh_token, spotify_user_id
from refresh import Refresh
import time

class Player(object):
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ''
        self.device_id = ''
        self.music_playing = False

    def start_music(self):
        '''
        Starts music from where the user last left off
        '''
        self.call_refresh()
        self.device()
        query = f'https://api.spotify.com/v1/me/player/play?device_id={self.device_id}'
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.spotify_token}'
        }
        
        response = requests.put(query, headers=header)
        if response.ok:
            self.music_playing = True

    def pause_music(self):
        '''
        Pauses music from where the user last left off
        '''
        self.call_refresh()
        self.device()
        query = f'https://api.spotify.com/v1/me/player/pause?device_id={self.device_id}'
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.spotify_token}'
        }
        
        response = requests.put(query, headers=header)
        if response.ok:
            self.music_playing = False
  
    def device(self):
        '''
        Pauses music from where the user last left off
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
        refresh_caller = Refresh()
        self.spotify_token = refresh_caller.refresh()


if __name__ == '__main__':
    songs = Player()
    songs.device()
    songs.start_music()
    time.sleep(5)
    songs.pause_music()

