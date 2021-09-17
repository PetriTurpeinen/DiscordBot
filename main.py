import discord
#from discord.ext import commands
import os
import files
import quizmethods
from keepalive import keep_alive
import replitdatabase

client = discord.Client()

#Variables
#Used to check if quiz is active, set to off by default.
quizState = ".quizoff"
#--------------
#Instances
#--------------
#File handling:
#--------------
#Make instace of files class
file = files.Files("questions.txt")
#Read a file
questions = file.readFile()
databasevalues = replitdatabase.Database()
#---------------
#Quizmethods
#---------------
#Make instance of quizmethod class to get a random question
quizmethod = quizmethods.QuizMethods(questions)
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
 
  if message.content.startswith(".quizstate"):
    await message.channel.send(quizState) 

  if message.content.startswith(".quizoff"):
    quizState = ".quizoff"
    await message.channel.send("You have set quiz off.")    

  #Start quiz and ask a random question
  if message.content.startswith(".quizon") and quizState == ".quizoff":
    quizState = ".quizon"    
    await message.channel.send("You have set quiz on.")           
    await message.channel.send(quizmethod.askRandomQuestion())  


  #Congratulate user for right answer and keep asking questions
  if message.content == databasevalues.getAnswer() and quizState == ".quizon":    
    databasevalues.addUserDB(message.author.name)
    #Message sent to the user if he/she answers correctly  
    correctmsg = "That was correct answer. You have now: " + str(databasevalues.getPoints(message.author.name)) + " points"    
    await message.channel.send(correctmsg)     
    await message.channel.send(quizmethod.askRandomQuestion())   

#---------------
#Discord bot token
my_secret = os.environ['TOKEN']
#Just a function to keep the bot alive by pinging it every 5 minutes
keep_alive()
client.run(os.getenv('TOKEN'))
#TODO
#Add correct msg to quiz methods
#Make database class and move database code there












    

    

