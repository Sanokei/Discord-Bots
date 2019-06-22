import discord
import asyncio
import time
import random
import os
#Made by SanoKei

token = "TOKEN"
#List to do
'''
1.Gambling command
2.Economy
3.Command to see how much money you have
4.Command to settle a bet
5.Economic hiarchy (bal top)
6.make sure who was betting and who got bet
7.Notify winner
8.Money exchange between people
9.
'''


#login
bot = discord.Client()

#log in message
@bot.event
async def on_ready():
    print("Name: " + bot.user.name)
    print("ID: " + bot.user.id)
    print('------------------------')

#call on bot to take bet
@bot.event
async def on_message(message):
    #--------------------------------------#
    with open("Bets.txt") as f:
        count = len(f.readlines())
    count = int(count)
    MESSAGE = message.content.lower()
    #----------------info------------------#
    if(MESSAGE == "#bet"):
        await bot.send_message(message.channel, "Please use the command properly, do \"#bet help\" for more infomation")
        return
    if(MESSAGE == "#bet help" or MESSAGE == "#bet ?"):
        await bot.send_message(message.channel, "To set a new Bet simply type: \n#bet (bet contents) $ammount !Bet against \nEx: \n#bet (eat an apple) $1 !William\n\nTo Search a Bet that has already simply type: \n#bet Search: Id of the bet \nEx: \n#bet Search: 420")
        return
    #--------------------------------------#
    if("#bet" in MESSAGE):
    #Set a bet
      if("(" in MESSAGE and ")" in MESSAGE and "$" in message.content):
        #-----Isolating the money-----#
        INDEX = MESSAGE.index("!")
        ammount = ""
        INDEX += 1
        while(INDEX < len(MESSAGE)):
            USER +=  MESSAGE[INDEX]
            INDEX += 1
        #-----Isolating the money-----#
        INDEX = MESSAGE.index("$")
        LAST = MESSAGE.index("!")
        ammount = ""
        INDEX += 1
        while(INDEX < LAST:
            ammount +=  MESSAGE[INDEX]
            INDEX += 1
        #----Isolating the Bet----#
        INDEX = MESSAGE.index("(")
        LAST = MESSAGE.index(")")
        bet = ""
        INDEX += 1
        while(INDEX < LAST):
            bet +=  MESSAGE[INDEX]
            INDEX += 1
        #----Writing down the bet in a file----#
        file = open('Bets.txt','a+')
        r_id = await self.get_user_info(message.author.id)
        sentence = ("{}.[\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"false\",\"false\",\"false\",\"false\"]".format(count,count,bet,ammount,s_id,r_id))
        file.write(sentence + '\n')
        await bot.send_message(message.channel,"Sucess! Your bet has been set your id number is {}".format(count))
          file.close
          return
      #----Error Message to check if ----#
      elif("search:" not in MESSAGE and "settle:" not in MESSAGE):
          await bot.send_message(message.channel, "Error: I did not understand that. Please type \'#bet help\' for more infomation")
          return
      #Search a bet
          if("search:" in MESSAGE):
              INDEX = MESSAGE.index(":")
              id_num = ""
              INDEX += 1
              while(INDEX < len(MESSAGE)):
                  id_num +=  MESSAGE[INDEX]
                  INDEX += 1
              id_num.replace(" ","")
              id_num = int(id_num) + 1
              if(id_num > count or id_num < 0):
                  await bot.send_message(message.channel, "Error: The number you inputted was outside the supported area.")
                  return
              sentence = open('Bets.txt').read().splitlines()
              await bot.send_message(message.channel, sentence[id_num - 1])
              return
          elif("settle:" not in MESSAGE):
              await bot.send_message(message.channel, "Error: Not a valid number. Please type \'#bet help\' for more infomation")
              return
      #Settle a bet
          if("settle:" in MESSAGE):
              INDEX = MESSAGE.index(":")
              id_num = ""
              INDEX += 1
              while(INDEX < len(MESSAGE)):
                  id_num +=  MESSAGE[INDEX]
                  INDEX += 1
              id_num.replace(" ","")
              id_num = int(id_num) + 1
              if(id_num > count or id_num < 0):
                  await bot.send_message(message.channel, "Error: The number you inputted was outside the supported area.")
                  return
              sentence = open('Bets.txt').read().splitlines()
              if(message.authour.id  not in sentence[id_num - 1]):
                  await bot.send_message(message.channel, "Error: You do not have permission to this bet")
                  return
              else:

              return
          else:
              await bot.send_message(message.channel, "Error: Not a valid number. Please type \'#bet help\' for more infomation")
              return
bot.run(token)
        
