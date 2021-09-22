import discord
#from discord.ext import commands
import os
#import files
import quizmethods
from keepalive import keep_alive
import replitdatabase

client = discord.Client()

#Variables
#List for questions & answers
qlist = [[],[],[]]
#Used to check if quiz is active, set to off by default.
quizState = ".quizoff"
qAmount = []
counter = 0
#--------------
#Instances
#--------------
databasevalues = replitdatabase.Database()

#---------------
#Quizmethods
#---------------
#Make instance of quizmethod class to get a random question
quizmethod = quizmethods.QuizMethods()
#---------------
# Discord events
#---------------

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  global quizState
  global qlist
  global counter
  global qAmount
 #Check whether quiz is on/off
  if message.content == ".quizstate":
    await message.channel.send(quizState)

  if message.content == ".help":
    await message.channel.send("You can start the quiz by typing .quizon and number of questions (20 is maxmimum). For example: .quizon 4 .") 

  if message.content == ".quizoff":
    quizState = ".quizoff"
    await message.channel.send("You have set quiz off.")    
  try:
    if message.content.startswith(".quizon") and quizState == ".quizoff":
      qAmount = message.content.split(" ")
      if qAmount[1].isnumeric():
        quizState = ".quizon"    
        await message.channel.send("You have set quiz on.")
        qlist = quizmethod.askOpenTriviaQuestions(int(qAmount[1]))          
        await message.channel.send(qlist[0][counter])               
        await message.channel.send(qlist[2][counter])      
      else:
        await message.channel.send("Please enter a numeric value after the question. For example: .quizon 4")
  except:
    await message.channel.send("You need to enter the amount of questions. For example: .quizon 4")



  #Congratulate user for right answer and keep asking questions
  if message.content == qlist[1][counter] and quizState == ".quizon" and counter < int(qAmount[1]):    
    databasevalues.addUserDB(message.author.name)
    #Message sent to the user if he/she answers correctly  
    correctmsg = "That was correct answer " + message.author.name + "! You have now: " + str(databasevalues.getPoints(message.author.name)) + " points"    
    await message.channel.send(correctmsg)
    if counter < int(qAmount[1]) - 1:
      counter += 1        
      await message.channel.send(qlist[0][counter])      
      await message.channel.send(qlist[2][counter])
    else:
      quizState = ".quizoff"
      counter = 0
      await message.channel.send("Quiz has ended.")           

#---------------
#Discord bot token
my_secret = os.environ['TOKEN']
#Just a function to keep the bot alive by pinging it every 5 minutes
keep_alive()
client.run(os.getenv('TOKEN'))

#Legacy code
#Start quiz and ask a random question (reads qustions from text file)
  #if message.content == ".quizon" and quizState == ".quizoff":
    #quizState = ".quizon"    
    #await message.channel.send("You have set quiz on.")           
    #await message.channel.send(quizmethod.askRandomQuestion()
#File handling:
#--------------
#Make instace of files class
#file = files.Files("questions.txt")
#Read a file
#questions = file.readFile()












    

    

