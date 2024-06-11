import nltk
from nltk.tokenize import word_tokenize


class TextManipulator:
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        return word_tokenize(self.text)

    def pos_tag(self):
        return nltk.pos_tag(self.tokenize())

    def __str__(self):
        return self.text
