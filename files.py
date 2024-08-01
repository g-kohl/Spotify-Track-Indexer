from APIcalls import *
import struct
import unicodedata

def makeArtistfromJSON(artistJSON):
    artistJSON = json.loads(artistJSON)

    return Artist(artistJSON["id"], artistJSON["name"], artistJSON["popularity"], artistJSON["followers"]["total"], artistJSON["genres"], artistJSON["external_urls"])


def makeArtist(artistString):
    attributes = decodeString(artistString)

    return Artist(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])


def encodeASCII(object):
    objectString = str(object)

    return unicodedata.normalize('NFKD', objectString).encode('ASCII', 'ignore')


def decodeString(artistString):
    return artistString.split("*")


def writeInBinaryFile(file, string):
    file.write(struct.pack('I', len(string)))
    file.write(string)


def readFromBinaryFile(fileName, quantity):
    listOfStrings = []

    with open(fileName, 'rb') as f:
        for _ in range(quantity):
            stringSize = struct.unpack('I', f.read(4))[0]
            string = f.read(stringSize)

            listOfStrings.append(string.decode('ASCII', 'ignore'))

    f.close()

    return listOfStrings