from Question import *


class Vocab(Question):
    __slots__ = ['correctAnswer', 'text']

    def __init__(self, correctAnswer, text):
        self.correctAnswer = correctAnswer
        self.text = text

    def ask(self):
        print(self.text)
        return input(">> ").lower()