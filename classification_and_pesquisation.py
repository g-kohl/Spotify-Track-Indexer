from files import *
from models.track import Track


class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    # Inserts in B-tree
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    # Auxiliar function for "insert"
    def insert_non_full(self, x, k):
        if any(key[0] == k[0] for key in x.keys):
            return

        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        elif not x.leaf:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    # Auxiliar function for "insert"
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    # Returns searched key
    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return x.keys[i][1]
                # return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])
        else:
            return self.search_key(k, self.root)


class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.pointer = None
        self.children = dict()
        self.is_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    # Inserts in TRIE
    def insert(self, word, pointer):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True
        current.pointer = pointer

    # Returns searched word
    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]

        if current.is_word:
            return current

    # Returns list of words matching the specified prefix
    def starts_with(self, prefix):
        pointers = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                return list()
            current = current.children[char]

        self.__child_words_for(current, pointers)
        return pointers
    
    # Auxiliar function for "starts_with"
    def __child_words_for(self, node, pointers):
        if node.is_word:
            pointers.append(node.pointer)
        for letter in node.children:
            self.__child_words_for(node.children[letter], pointers)


# Creates dictionary for inverted file
def init_popularity_table():
    dictionary = {}

    for i in range(101):
        dictionary[i] = []

    return dictionary


# Sorts a list of tracks based on the specified attribute
def sort_track_list(tracks, attribute, low, high):
    if low < high:
        pi = partition(tracks, attribute, low, high)
 
        sort_track_list(tracks, attribute, low, pi - 1)
        sort_track_list(tracks, attribute, pi + 1, high)


# Auxiliar function for "sort_track_list"
def partition(list, attribute, low, high):
    pivot = list[high]
    i = low - 1

    for j in range(low, high):
        if (attribute == "0" and list[j].popularity <= pivot.popularity or
            attribute == "1" and list[j].name <= pivot.name or
            attribute == "2" and list[j].artist_name <= pivot.artist_name):

            i = i + 1

            (list[i], list[j]) = (list[j], list[i])

    (list[i + 1], list[high]) = (list[high], list[i + 1])
 
    return i + 1