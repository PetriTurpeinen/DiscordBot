from replit import db

class Database():  

  def getQuestion(self):
    return db["question"]

  def getAnswer(self):
    return db["answer"]
  
  def addValues(self, question, answer):
    db["question"] = question
    db["answer"] = answer