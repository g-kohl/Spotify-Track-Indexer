import unicodedata
import pickle


def encode_ASCII(object):
    object_string = str(object)

    return unicodedata.normalize('NFKD', object_string).encode('ASCII', 'ignore')


def write_in_binary_file(obj, file):
    pickle.dump(obj, file)


def read_from_binary_file(file):
    return pickle.load(file)
