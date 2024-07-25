import requests
import json
import os
from dotenv import load_dotenv
# from collections import namedtuple
from models import *
import struct
# from pprint import pprint

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


# def artistJSONtoObj(artistDictionary):
#     return namedtuple('X', artistDictionary.keys())(*artistDictionary.values())


def makeArtistObj(artistJSON):
    artistJSON = json.loads(artistJSON)

    return Artist(artistJSON["id"], artistJSON["name"], artistJSON["popularity"], artistJSON["followers"]["total"], artistJSON["genres"], artistJSON["external_urls"])


token = getAccessToken()

artistJSON = requests.get(
    "https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw",
    headers=authorizationHeader(token),
)

artistExample = makeArtistObj(artistJSON.text)

artistString = str(artistExample)
artistStringBin = artistString.encode('utf-8')

with open('binaryFileEx.bin', 'wb') as f:
    f.write(struct.pack('I', len(artistStringBin)))
    f.write(artistStringBin)

with open('binaryFileEx.bin', 'rb') as f:
    stringSize = struct.unpack('I', f.read(4))[0]

    artistStringBin = f.read(stringSize)
    artistString = artistStringBin.decode('utf-8')

f.close()

print(artistString)
