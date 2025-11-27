import datetime
import os

import dotenv
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv()
CLIENT_ID = os.getenv("BILLBOARD_TO_SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("BILLBOARD_TO_SPOTIFY_CLIENT_SECRET")
SPOTIFY_USER_ID = os.getenv("SPOTIFY_USER_ID")
SPOTIFY_USER_TOKEN = os.getenv("SPOTIFY_USER_TOKEN")


def get_current_top_100_titles():
    header = {"USER-AGENT": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0"}
    url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.select("div.o-chart-results-list-row-container li.a-chart-result-item-container h3#title-of-a-story")
    return [row.get_text().strip() for row in rows]


def get_tracks_urls(titles):
    result = []
    for title in titles:
        track = spotify.search(q=title, limit=1)
        result.append(track["tracks"]["items"][0]["external_urls"]["spotify"])

    return result


def create_playlist():
    date = datetime.date.today()
    playlist = spotify.user_playlist_create(user=SPOTIFY_USER_ID, name=f"{date} Billboard Top 100", public=False)
    return playlist["id"]


def add_tracks(playlist_id_, tracks_urls_):
    spotify.playlist_add_items(playlist_id=playlist_id_, items=tracks_urls_)


spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="https://example.com/",
                              scope="playlist-modify-private"))

top_100_titles = get_current_top_100_titles()
tracks_urls = get_tracks_urls(top_100_titles)
playlist_id = create_playlist()

add_tracks(playlist_id, tracks_urls)
