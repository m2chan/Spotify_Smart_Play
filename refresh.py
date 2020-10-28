# Refreshes the Spotify API token

from config import refresh_token, base_64_id
import requests

class Refresh(object):
    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64_id = base_64_id

    def refresh(self):
        query = 'https://accounts.spotify.com/api/token'
        
        header = {
            'Authorization': f'Basic {base_64_id}'
        }
        
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
        
        response = requests.post(query, data=data, headers=header)
        response_json = response.json()

        return response_json['access_token']

if __name__ == '__main__':
    refresh = Refresh()
    print(refresh.refresh())