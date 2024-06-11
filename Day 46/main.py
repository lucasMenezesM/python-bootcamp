from bs4 import BeautifulSoup
from pprint import pprint
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from MusicScraper import MusicScraper
from spotify_manager import SpotifyManager

music_scraper = MusicScraper()
year = input("Choose a year")
music_scraper.scrape_musics_by_year(year=year)
titles_list = music_scraper.music_list
print(titles_list)

spotify_manager = SpotifyManager()
playlist = spotify_manager.create_playlist(name=f"{year} Top Songs")
playlist_id = playlist["id"]

uri_list = []

for music in titles_list:
    uri = spotify_manager.get_uri(track=music, year=year)
    uri_list.append(uri)

print(uri_list)

print(spotify_manager.add_items_to_playlist(items=uri_list, playlist_id=playlist_id))


