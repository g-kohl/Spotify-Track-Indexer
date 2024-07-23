import requests
import json
import os
from dotenv import load_dotenv
from collections import namedtuple
# import SimpleNamespace as Namespace


# class Artist:
#     def __init__(self, id, name, popularity, followers, genres, external_URLs):
#         self.id, self.name, self.popularity, self.followers, self.genres, self.external_URLs = id, name, popularity, followers, genres, external_URLs


load_dotenv()

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")


def getAccessToken():
    token = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data="grant_type=client_credentials&client_id={}&client_secret={}".format(
            clientId, clientSecret
        ),
    )
    if not token:
        raise Exception("Error fetching validation token.")

    access_token = json.loads(token.text)["access_token"]
    if not access_token:
        raise Exception("Invalid access_token")

    return access_token


def authorizationHeader(token):
    return {"Authorization": "Bearer " + token}


def makeArtist(artistDictionary):
    return namedtuple('X', artistDictionary.keys())(*artistDictionary.values())


token = getAccessToken()

artistObj = requests.get(
    "https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw",
    headers=authorizationHeader(token),
)

# artist = json.loads(artistObj.text)

artist = json.loads(artistObj.text, object_hook=makeArtist)

print(artist.name, artist.popularity)
