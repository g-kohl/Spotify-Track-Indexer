from API_calls import *
import struct
import unicodedata
from models.artist import Artist

def make_artist_from_JSON(artist_JSON):
    artist_JSON = json.loads(artist_JSON)

    return Artist(artist_JSON["id"], artist_JSON["name"], artist_JSON["popularity"], artist_JSON["followers"]["total"], artist_JSON["genres"], artist_JSON["external_urls"])


def make_artist(artist_string):
    attributes = decode_string(artist_string)

    return Artist(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])


def encode_ASCII(object):
    object_string = str(object)

    return unicodedata.normalize('NFKD', object_string).encode('ASCII', 'ignore')


def decode_string(artist_string):
    return artist_string.split("*")


def write_in_binary_file(file, string):
    file.write(struct.pack('I', len(string)))
    file.write(string)


def read_from_binary_file(file_name, quantity):
    list_of_strings = []

    with open(file_name, 'rb') as f:
        for _ in range(quantity):
            string_size = struct.unpack('I', f.read(4))[0]
            string = f.read(string_size)

            list_of_strings.append(string.decode('ASCII', 'ignore'))

    f.close()

    return list_of_strings