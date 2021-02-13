from abc import ABC, abstractmethod 


class Question:
    __slots__ = ['correctAnswer', 'text']
    def __init__(self, correctAnswer, text):
        self.correctAnswer = correctAnswer
        self.text = text

    def score(self, answer):
        return answer.lower() == self.correctAnswer.lower()


    @abstractmethod
    def ask(self):
        pass


    