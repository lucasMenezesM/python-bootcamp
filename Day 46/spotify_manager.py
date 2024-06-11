from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy

config = dotenv_values("Day 46/.env")

scope= "playlist-modify-private"
create_playlist_endpoint = f"https://api.spotify.com/v1/users/{config['user_id']}/playlists"

class SpotifyManager:
    def __init__(self) -> None:
        auth = SpotifyOAuth(client_id=config["spotify_client_id"], client_secret=config["spotify_client_secret"], scope=scope, redirect_uri="https://example.com/", cache_path="Day 46/token.txt")

        self.sp = spotipy.Spotify(auth_manager=auth)
        
    
    def create_playlist(self, name: str) -> None:
        return self.sp.user_playlist_create(user=config["user_id"], public=False, description="A playlist", collaborative=False, name=name)


    def get_uri(self, track: str, year) -> str:
        print(f"Loading {track} uri...")
        results = self.sp.search(q=f"track: {track} year: {year}", type="track")
        track = results["tracks"]["items"][0]["uri"]
        return track


    def get_track(self, track_id):
        return self.sp.track(track_id=track_id)
    

    def add_items_to_playlist(self, items: list, playlist_id: str):
        return self.sp.playlist_add_items(playlist_id=playlist_id, items=items)