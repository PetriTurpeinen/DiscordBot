import random
#import replitdatabase
import json
import requests
import html
#Class made for a quiz bot
class QuizMethods():  

  def __init__(self):
    pass
    
  #https://opentdb.com/api_config.php
  #Get a random question from open trivia database
  def askOpenTriviaQuestions(self,amount):
    
    qMatrix = [[""]*amount,[""]*amount,[""]*amount]

    for i in range(0,amount):
      #Add question, right answer and choices to matrix
      qList = self.get_question()
      qMatrix[0][i] = qList[0]
      qMatrix[1][i] = qList[1]
      qMatrix[2][i] = qList[2]
    return qMatrix

  def get_question(self):
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    json_data = json.loads(response.text)
    question = html.unescape(json_data["results"][0]["question"])
    right_answer = html.unescape(json_data["results"][0]["correct_answer"])
    wrong_answers = html.unescape(json_data["results"][0]["incorrect_answers"])
    choices = []
    str_choices = "Choices: "
    for i in range(0,len(wrong_answers)):
      if i == 0:
        choices.append(html.unescape(str(right_answer)))
        choices.append(html.unescape(str(wrong_answers[i])))
      else:
        choices.append(html.unescape(str(wrong_answers[i])))

    random.shuffle(choices)

    for j in range (0,len(choices)):
      if j != len(choices) -1:
        str_choices += str(choices[j]) + ", "
      else:
        str_choices += str(choices[j])
        
    qList = []
    qList.append(question)
    qList.append(right_answer)
    qList.append(str_choices)    

    return(qList)

#Legacy code
  #Choose a random question and return the question
  #def askRandomQuestion(self):

  #   databasevalues = replitdatabase.Database()
  #   randomquestion = self.randomQuestion()
  #   question = randomquestion[0]
  #   answer = randomquestion[1]
  #   databasevalues.addValues(question,answer)
  #   databasevalues.getQuestion()

#legacy code
  #Choose a random question
  #def randomQuestion(self):
  #  question_answer = random.choice(self.questions)
  #  split_question_answer = question_answer.split("|")    
  #  return split_question_answer
  #return databasevalues.getQuestion()

