import requests
import json
import os
from dotenv import load_dotenv
# from collections import namedtuple
from models import *
import struct
import unicodedata
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


def encodeUTF8(object):
    objectString = str(object)

    return unicodedata.normalize('NFKD', objectString).encode('ASCII', 'ignore')


def writeInBinaryFile(fileName, string):
    with open(fileName, 'wb') as f:
        f.write(struct.pack('I', len(string)))
        f.write(string)


def readFromBinaryFile(fileName):
    with open(fileName, 'rb') as f:
        stringSize = struct.unpack('I', f.read(4))[0]
        string = f.read(stringSize)

    f.close()

    return string.decode('utf-8', 'ignore')


token = getAccessToken()

artistJSON = requests.get(
    "https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw",
    headers=authorizationHeader(token),
)

artistExample = makeArtistObj(artistJSON.text)
artistStringBin = encodeUTF8(artistExample)

writeInBinaryFile('binaryFileEx.bin', artistStringBin)
artistString = readFromBinaryFile('binaryFileEx.bin')

print(artistString)
