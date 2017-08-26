#Orsik, Dwarf male, operator of the Empty Tankard


#Client ID 349695599186280448

#To add to a server, https://discordapp.com/oauth2/authorize?client_id=349695599186280448&scope=bot&permissions=0

import discord
from discord.ext import commands
import asyncio
import random

#Utility Function to get the token from the file
def gettoken(file):
    with open(file) as f:
        for line in f:
            token=str(line)
    return token


bot = discord.Client()

bot_prefix= "q-"


targetchannel = 'null' #inital setting prior to in-Discord reset

bot = commands.Bot(command_prefix=bot_prefix)



#@bot.event
#async def on_resume():
#    await bot.send_message(chnl, 'Sorry, drifted off there.')


@bot.event
async def on_message(msg):
    
#Check to avoid loop or command bot
    if msg.author == bot.user or msg.content.startswith(bot_prefix):
        return

    elif msg.content.startswith('$targetchannel'):
        targetchannel = msg.channel
        response = '/`Orsik will respond with In-Character messages in {0}/`'.format(str(targetchannel))
        bot.send_message(msg.channel, response)

#In character interactions
    elif msg.content.startswith('Orsik'):
        
        user = msg.author
        name = user.display_name

        if targetchannel != str(msg.channel):
            response = '/`Orsik BOT has not been assigned to {}/`'.format(str(targetchannel))
            bot.send_message(msg.channel, response)
            return

        elif msg.content.find('Flint') and msg.content.find('?'):
            response = 'Flint, not a better Dwarf to fight alongside.'
            
        else:
            ya = random.choice(affirm)
            aid = random.choice(assit)
            response =  '{0} {1}, how can I {2} you?'.format(ya.capitalize(), name.capitalize(), aid)
           
    else:
        return
    
    await bot.send_message(targetchannel, response)

#@bot.event
#async def on_member_update(old_state,new_state):
#    hello = '{0} to the Empty Tankard, have a seat.  My name\'s Orsik'.format(random(greetings))

#    await bot.send_message(hello)

@bot.command(name='close') #not currently working
async def close(ctx):
#    await bot.send_message(ctx.channel, "Closing down folks.")
    await bot.close()

@bot.event
async def on_ready():
    print("-------")
    print("Orsik is behind the bar.")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("-------")
    #Indicate how to interact
    await bot.change_presence(game=discord.Game(name='Behind the bar'))
    

#Source List and Tuples
greetings = ["hello", "hi", "hey", "good day"]

affirm = ["yes", "aye", "ya"]

assit = ["help", "aid", "assist"]

nr_actions = ["_is cleaning out a recently finished tankard._",
              "_wipes down the bar._", "_seems to be in deep thought._"]

inns = [("Old Hold",  "Lower City", "near the Gate", "Dwarfs", ""),
        ("Blushing Mermaid", "Lower City", "northeast", "shady"),
        ("Blade and Stars", "Lower City", "southeast", "comfortable", ),
        ("Helm and Cloak", "Upper City", "northwest", "luxury", "expensive"),
        ("Splurging Sturgeon", "Lower City", "northeast", "good",  "cheap" ),
        ("Purple Wyrm Inn and Tavern","Lower City", "central", "quality", "what you would expect"),
        ("Three Old Kegs", "Upper City", "east wall of the Ducal Palace", "excellent", "good")]

taverns = [("Elfsong Tavern", "Lower City", "southeast", "quality, but haunting", "bit pricy")]

drinks = ["Mithral Ale", "Local Ale", "Meade"]


token=gettoken("orsiktoken") #Token is stored in a separate file and pulled for the call

bot.run(token) 


