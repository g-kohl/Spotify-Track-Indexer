from files import *
from dotenv import load_dotenv


load_dotenv()

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

token = getAccessToken(clientId, clientSecret)

artistJSON = requests.get(
    "https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02?si=_SxFzIqhTXSMtPUdvBseLw",
    headers=authorizationHeader(token),
)

artistExample = makeArtistfromJSON(artistJSON.text)
artistStringBin = encodeASCII(artistExample)

print(artistStringBin)
writeInBinaryFile('binaryFileEx.bin', artistStringBin)
# writeInBinaryFile('binaryFileEx.bin', artistStringBin)

# listOfArtists = readFromBinaryFile('binaryFileEx.bin', 2)

# newArtist1 = makeArtist(listOfArtists[0])
# newArtist2 = makeArtist(listOfArtists[1])