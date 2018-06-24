import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
#Made by Sano
count = 0
#
#login
Client = discord.Client()
bot = commands.Bot(command_prefix = "")

#log in message
@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name)
    print("ID: " + bot.user.id)
    print('------')
#
@bot.event
async def on_ready():
	for line in open('WilliamLog.txt').xreadlines(  ):
		count += 1
#On event
@bot.event
async def on_message(message):
#command to say something i would say
whitelist = ["whitelisted people id"]
	if message.content == "WilliamBot" :
		file = open('WilliamLog.txt', 'r+')
		print(count)
		RanLine = random.randrange(count) + 1
		print(RanLine)
		Line = file.readline(RanLine)
		await bot.send_message(message.channel,Line)
		file.close

#checking if I wrote a message, then adding it to a file

	print(message.author.id)
	if (message.author.id in whitelist) and (message.content != "Bot name"):
		print("William wrote a message")
		file = open('WilliamLog.txt','a+')
		Message = message.content
		file.write(Message + '\n')
		file.close
		
		
#run
bot.run("Api Key")
