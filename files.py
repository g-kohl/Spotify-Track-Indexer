import unicodedata
from models.artist import Artist
import pickle
import json

def make_artist_from_JSON(artist_JSON):
    artist_JSON = json.loads(artist_JSON)

    return Artist(artist_JSON["id"], artist_JSON["name"], artist_JSON["popularity"], artist_JSON["followers"]["total"], artist_JSON["genres"])


def make_artist(artist_string):
    attributes = decode_string(artist_string)

    return Artist(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4])


def encode_ASCII(object):
    object_string = str(object)

    return unicodedata.normalize('NFKD', object_string).encode('ASCII', 'ignore')


def decode_string(artist_string):
    return artist_string.split("*")


def write_in_binary_file(obj, file):
    pickle.dump(obj, file)


def read_from_binary_file(file):
    return pickle.load(file)