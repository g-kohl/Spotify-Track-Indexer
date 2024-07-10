import requests
import json

clientId = "f56c4d0716ca4c8e872d14e0914a6c8c"
clientSecret = "2b7a100fda8d42a2833ad8cedab1567e"

def getAccessToken():
    token = requests.post("https://accounts.spotify.com/api/token", 
                      headers = {"Content-Type": "application/x-www-form-urlencoded"},
                      data = "grant_type=client_credentials&client_id={}&client_secret={}".format(clientId, clientSecret))
    if not token:
        raise Exception("Error fetching validation token.")

    access_token = json.loads(token.text)['access_token']
    if not access_token:
        raise Exception("Invalid access_token")

    return access_token

def authorizationHeader(token):
    return {"Authorization": "Bearer " + token}

token = getAccessToken()

artistObj = requests.get("https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw", headers = authorizationHeader(token))

artist = json.loads(artistObj.text)

print(artist)
