from Question import * 


class MultipleChoice(Question):
    __slots__ = ['correctAnswer', 'text', 'options', 'num_options']

    def __init__(self, correctAnswer, text):
        self.correctAnswer = correctAnswer
        self.text = text
        self.options = dict()
        self.num_options = 0

    def addOption(self, text):
        self.options[chr(self.num_options + 65)] = text
        self.num_options += 1


    def ask(self):
        print(self.text)
        for i in range(len(self.options)):
            letter = chr(i + 65)
            print(letter, ":", self.options[letter])
        return input(">> ").lower()
