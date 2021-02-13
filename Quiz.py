from TrueFalse import TrueFalse
from Question import *
from TrueFalse import *
from MultipleChoice import *
from Vocab import *


class Quiz:
    __slots__ = ['questionList', 'incorrectList']

    def __init__(self):
        self.questionList = []
        self.incorrectList = []

    def addQuestion(self, question):
        self.questionList.append(question)

    def displayWrongQuestions(self):
        while len(self.incorrectList) > 0:
            for wrongQuestion in self.incorrectList:
                answer = wrongQuestion.ask()
                if wrongQuestion.score(answer):
                    print('Correct')
                    input("Press Enter to Continue: ")
                    self.incorrectList.remove(wrongQuestion)
                else:
                    print('Incorrect')
                    input("Press Enter to Continue: ")

    def gradeQuiz(self):
        numQuestions = len(self.questionList)
        numCorrectQuestions =  numQuestions - len(self.incorrectList)
        print("You got ", numCorrectQuestions, "/", numQuestions, " correct", sep="")
        input("Press Enter to Continue: ")

    def takeQuiz(self):
        for question in self.questionList:
            answer = question.ask()
            if question.score(answer):
                print("Correct")
            else:
                print("Incorrect")
                self.incorrectList.append(question)
            input("Press Enter to Continue: ")
        self.gradeQuiz()
        self.displayWrongQuestions()
        print("GoodBye")

    