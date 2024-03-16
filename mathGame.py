import random
import math


class Question():
    def __init__(self, q, a):
        self.question = q
        self.answer = a

    def __str__(self):
        return self.question

    def checkAnswer(self, ans) -> bool:
        return self.answer.lower() == ans.lower()

    def setQuestionBody(self, body) -> None:
        self.question = body

    def setAnswer(self, ans) -> None:
        self.answer = ans

    def getAnswer(self):
        return self.answer


class Player():
    def __init__(self, n):
        self.name = n
        self.score = 0
        self.question = 0
        self.questionBankFile = "questionBank.txt"

    def getQuestion(self):
        questionList = []
        answerList = []
        try:
            with open(self.questionBankFile, 'r') as file:
                flipFlop = 2
                for line in file:
                    if flipFlop%2 == 0:
                        questionList.append(line.strip())
                    else:
                        answerList.append(line.strip())
                    flipFlop += 1
        except FileNotFoundError:
            print("This Player was given an invalid file to derive questions from.")
        index = random.randint(0, len(questionList)-1)
        q = Question(questionList[index], answerList[index])
        self.question = q
        
    def askQuestion(self):
        correctAnswer = False
        print("--------------------------------------------")
        print(self.question)
        answer = input(">>> ")
        result = self.question.checkAnswer(answer)
        while not result:
            print("Not quite. 'new' = see the answer and get a new question")
            print("Question:", self.question)
            answer = input(">>> ")
            if answer.lower() == 'new':
                print('Answer:', self.question.getAnswer())
                print("overwrite = Overwrite: I was correct | Enter anything else to continue")
                response = input(">>> ")
                if response.lower() == "overwrite":
                    correctAnswer = True
                    result = True
                    self.getQuestion()
                if not correctAnswer:
                    self.getQuestion()
                    break
            else:
                result = self.question.checkAnswer(answer)
                if result:
                    correctAnswer = True
        if correctAnswer:
            print("Correct!")
            self.score += 1

    def getScore(self):
        return self.score
    
    
class Driver():
    def __init__(self):
        pass

    def beginGame(self):
        playing = True
        print("Let's Play!")
        p1 = Player('Josiah')
        p1.getQuestion()
        p1.askQuestion()
        while playing:
            print("Would you like another question? y/n")
            response = input(">>> ")
            if response.lower() in ['no', 'nope', 'no way', 'no i do not']:
                break
            p1.askQuestion()
        print("Your final score is:", p1.getScore())


d = Driver()
d.beginGame()
