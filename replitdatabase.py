from replit import db
#Datbase class is used for storing user information
class Database():

#test purpose
  def delUser(self, user):
    del db[user] 

  #Add user to db and set his score to 1 if not in db, otherwise increase it by 1.
  def addUserDB(self, user):
    keys = db.keys()
    
    if user in keys:
      db[user] += 1
    else:
      db[user] = 1
  
   #Check how many points user has
  def getPoints(self, user):    
    return db[user]

#legacy code
#  def getQuestion(self):
#    return db["question"]

#  def getAnswer(self):
#   return db["answer"]

#Add quiz question and answer to database  
  #def addValues(self, question, answer):
  #  db["question"] = question
   # db["answer"] = answer
 