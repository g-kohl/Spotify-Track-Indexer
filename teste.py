from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id="2b488f116ad74deaa487b2645d143a8b",
                                               client_secret="6bf1f536d6d94c0ebb109dbf5ecd851a",
                                               redirect_uri="http://localhost:5001"))


results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])