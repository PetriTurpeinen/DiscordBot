import discord
#from discord.ext import commands
import os
import random
from replit import db
import files
import quizmethods
from keepalive import keep_alive
import replitdatabase

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
#--------------
#File handling:
#--------------
#Make instace of files class
file = files.Files("questions.txt")
#Read a text file
questions = file.readFile()
databasevalues = replitdatabase.Database()
#---------------
#Quizmethods
#---------------
#Make instance of quizmethod class to get a random question
quizmethod = quizmethods.QuizMethods(questions)
#---------------
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  correctmsg = "That is correct answer " + str(message.author.name) + "!"
  if message.content.startswith(".askquestion"):
    randomquestion = quizmethod.randomQuestion()
    question = randomquestion[0]
    answer = randomquestion[1]
    databasevalues.addValues(question, answer)         
    await message.channel.send(databasevalues.getQuestion())       
    
  if message.content.startswith(databasevalues.getAnswer()):
    await message.channel.send(correctmsg)  

my_secret = os.environ['TOKEN']
#Just a function to keep the bot alive by pinging it every 5 minutes
keep_alive()
client.run(os.getenv('TOKEN'))
#TODO
#Add correct msg to quiz methods
#Make database class and move database code there












    

    

