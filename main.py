import discord
#from discord.ext import commands
import os
import random
from replit import db
import files
import quizmethods
from keepalive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
#--------------
#--------------
#File handling:
#--------------
#Make instace of files class
file = files.Files("questions.txt")
#Read a text file
questions = file.readFile()
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
    db["question"] = question
    db["answer"] = answer                   
    await message.channel.send(db["question"])     
    #if msg == answer:
    #  await message.channel.send("Se oli oikein!")
    #else:
    #  await message.channel.send("Se oli väärin")
  #if message.content.startswith(".giveanswer"):
  #  await message.channel.send(db["answer"])
  if message.content.startswith(db["answer"]):
    await message.channel.send(correctmsg)  

my_secret = os.environ['TOKEN']
#Just a function to keep the bot alive by pinging it every 5 minutes
keep_alive()
client.run(os.getenv('TOKEN'))













    

    

