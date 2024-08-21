import unicodedata
import pickle


# Returns a object encoded in a string in ASCII 
def encode_ASCII(object):
    object_string = str(object)

    return unicodedata.normalize('NFKD', object_string).encode('ASCII', 'ignore')


# Writes object in binary file
def write_in_binary_file(obj, file):
    pickle.dump(obj, file)


# Reads object from binary file
def read_from_binary_file(file):
    return pickle.load(file)
