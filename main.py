from files import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

clientId = getenv("CLIENT_ID")
clientSecret = getenv("CLIENT_SECRET")

token = getAccessToken(clientId, clientSecret)

artistJSON = requests.get(
    "https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw",
    headers=authorizationHeader(token),
)

artistExample = makeArtistfromJSON(artistJSON.text)
artistStringBin = encodeASCII(artistExample)

file = open('binaryFileEx.bin', 'wb')
writeInBinaryFile(file, artistStringBin)
writeInBinaryFile(file, artistStringBin)
file.close()

listOfArtists = readFromBinaryFile('binaryFileEx.bin', 2)

newArtist1 = makeArtist(listOfArtists[0])
newArtist2 = makeArtist(listOfArtists[1])

print(newArtist1)
print(newArtist2)