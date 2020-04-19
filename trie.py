'''A node class for the Trie datastructure'''
class Node:

    def __init__(self):
        self.ref = [None for i in range(26)]
        self.mark = False

'''The Trie datastructure that has functions to add, delete and search for a certain word'''
class Trie:

    def __init__(self):
        self.root = Node()

    # Function that adds a word to the trie
    def add_word(self, word):
        word = word.lower()
        tmppoint = self.root
        length = len(word)
        for j in range(length):
            i = word[j]
            if tmppoint.ref[ord(i)-ord('a')] is None:
                tmppoint.ref[ord(i)-ord('a')] = Node()
            if j!= length-1:
                tmppoint = tmppoint.ref[ord(i)-ord('a')]
            else:
                tmppoint.mark = True
    
    # Function that returns True if a particular word is present in the trie else false
    def find_word(self, word):
        if not word.isalpha():
            return False
        word = word.lower()
        tmppoint = self.root
        length = len(word)
        for j in range(length):
            if tmppoint is None:
                return False
            i = word[j]
            if tmppoint.ref[ord(i)-ord('a')] is None:
                return False
            if j!= length-1:
                tmppoint = tmppoint.ref[ord(i)-ord('a')]
            else:
                return tmppoint.mark

    # Function that deletes a word from a Trie if it is present
    def delete_word(self, word):
        pass