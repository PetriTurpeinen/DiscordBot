from replit import db
#Datbase class is used for storing questions and user information
class Database():  

  def getQuestion(self):
    return db["question"]

  def getAnswer(self):
    return db["answer"]
 
  #test purpose
  #def delUser(self, user):
  #  del db[user]
  
#Add quiz question and answer to database  
  def addValues(self, question, answer):
    db["question"] = question
    db["answer"] = answer
  #Add user to db and set his score to 1 if not in db, otherwise increase it by 1.
  def addUserDB(self, user):
    keys = db.keys()
    if user != "question" and user != "answer":
      if user in keys:
        db[user] += 1
      else:
        db[user] = 1
  
   #Check how many points user has
  def getPoints(self, user):    
    return db[user]