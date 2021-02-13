from Quiz import *
from TrueFalse import TrueFalse
from Question import *
from TrueFalse import *
from MultipleChoice import *
from Vocab import *



TYPE_POSITION = 0
QUESTION_POSITION = 1
ANSWER_POSITION = 2
MULT_ANSWER_POSITION = -1

class QuizMaker:
    __slots__ = ['quiz']
    
    def __init__(self):
        self.quiz = Quiz()

    def parseQuestion(self, line, number):
        line = line.strip().split(',')
        if line[TYPE_POSITION] == 'T/F':
            question = TrueFalse(line[ANSWER_POSITION].strip(), line[QUESTION_POSITION])
            self.quiz.addQuestion(question)
        elif line[TYPE_POSITION] == 'V':
            question = Vocab(line[ANSWER_POSITION].strip(), line[QUESTION_POSITION])
            self.quiz.addQuestion(question)
        elif line[TYPE_POSITION] == 'M':
            question = MultipleChoice(line[MULT_ANSWER_POSITION].strip(), line[QUESTION_POSITION])
            for option in line[QUESTION_POSITION + 1:MULT_ANSWER_POSITION]:
                question.addOption(option)
            self.quiz.addQuestion(question)
        else:
            print("Unknown Question Type. Skipping Question on line", number)


    def readFile(self, filename):
        line_count = 1
        try:
            with open(filename) as file_:
                for line in file_:
                    if line != "\n":
                        self.parseQuestion(line, line_count)
                        line_count += 1
        except FileNotFoundError:
            print("Could not find that file. Double check the name and try again.")
        return self.quiz
