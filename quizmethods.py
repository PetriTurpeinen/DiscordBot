import random

class QuizMethods():

  def __init__(self, questions):
    self.questions = questions 

  def randomQuestion(self):
    question_answer = random.choice(self.questions)
    split_question_answer = question_answer.split("|")
    return split_question_answer

