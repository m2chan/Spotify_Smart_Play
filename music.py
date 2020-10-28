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
        self.music_playing = False
        self.tracks = ''

    def start_music(self):
        '''
        Starts music from where the user last left off
        '''

        query = 'https://api.spotify.com/v1/me/player/play'
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

        query = 'https://api.spotify.com/v1/me/player/pause'
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.spotify_token}'
        }
        
        response = requests.put(query, headers=header)
        if response.ok:
            self.music_playing = True
        

    def call_refresh(self):
        refresh_caller = Refresh()
        self.spotify_token = refresh_caller.refresh()
        self.start_music()
        time.sleep(5)
        self.pause_music()
        


if __name__ == '__main__':
    # songs = SaveSongs()
    # songs.find_songs()
    songs = Player()
    songs.call_refresh()

