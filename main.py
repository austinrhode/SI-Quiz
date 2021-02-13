from QuizMaker import *

def main():
    filename = input("Enter the name of the file: ")
    quizMaker = QuizMaker()
    quiz = quizMaker.readFile(filename)
    quiz.takeQuiz()


if __name__ == '__main__':
    main()
