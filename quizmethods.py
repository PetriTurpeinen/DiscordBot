import random
import replitdatabase
#Class made for a quiz bot
class QuizMethods():  

  def __init__(self, questions):
    self.questions = questions 

  #Choose a random question
  def randomQuestion(self):
    question_answer = random.choice(self.questions)
    split_question_answer = question_answer.split("|")    
    return split_question_answer

  #Choose a random question and return the question
  def askRandomQuestion(self):

    databasevalues = replitdatabase.Database()
    randomquestion = self.randomQuestion()
    question = randomquestion[0]
    answer = randomquestion[1]
    databasevalues.addValues(question,answer)
    databasevalues.getQuestion()

    return databasevalues.getQuestion()

