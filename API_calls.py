import requests
import json


def get_access_token(client_id, client_secret):
    token = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data="grant_type=client_credentials&client_id={}&client_secret={}".format(
            client_id, client_secret
        ),
    )
    if not token:
        raise Exception("Error fetching validation token.")

    access_token = json.loads(token.text)["access_token"]
    if not access_token:
        raise Exception("Invalid access_token")

    return access_token


def authorization_header(token):
    return {"Authorization": "Bearer " + token}