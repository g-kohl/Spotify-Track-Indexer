from files import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client_id = getenv("CLIENT_ID")
client_secret = getenv("CLIENT_SECRET")

token = get_access_token(client_id, client_secret)

# artist_JSON = requests.get(
#     "https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw",
#     headers=authorization_header(token),
# )