import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

def getToken():
    return requests.post("https://accounts.spotify.com/api/token", 
                      headers = {"Content-Type": "application/x-www-form-urlencoded"},
                      data = "grant_type=client_credentials&client_id={}&client_secret={}".format(clientId, clientSecret))

def getTokenString(token):
    return json.loads(token.text)['access_token']

def authorizationHeader(token):
    return {"Authorization": "Bearer " + token}

token = getTokenString(getToken())

artistObj = requests.get("https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw", headers = authorizationHeader(token))

artist = json.loads(artistObj.text)

print(artist)
