import requests
import json


def getAccessToken(clientId, clientSecret):
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