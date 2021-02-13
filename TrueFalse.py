from Question import *


class TrueFalse(Question):
    __slots__ = ['correctAnswer', 'text']

    def __init__(self, correctAnswer, text):
        self.correctAnswer = correctAnswer
        self.text = text

    def ask(self):
        while True:
            print("True or False?", self.text, "[t/f]")
            answer = input(">> ").lower()
            if answer != 'f' and answer != 't':
                print("Invalid response. Try Again.")
                continue
            return answer
