#Orsik, Dwarf male, operator of the Empty Tankard


#Client ID 349695599186280448

#To add to a server, https://discordapp.com/oauth2/authorize?client_id=349695599186280448&scope=bot&permissions=0

import discord
from discord.ext import commands
import asyncio

with open("orsiktoken") as f:
    for line in f:
        token=str(line)

bot = discord.Client()

bot_prefix= "!"
chnl="channel2" #change for deployment

bot = commands.Bot(command_prefix=bot_prefix)


@bot.event
async def on_ready():
    print("Orsik is behind the bar.")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    #Indicate how to interact
    await bot.change_presence(game=discord.Game(name='Call by name'))
    return

@bot.event
async def on_resume():
    await bot.send_message(chnl, 'Sorry, drifted off there.')
    return

#async def on_member_update(old_state,new_state):
#    await bot.send_message('Welcome to the Empty Tankard, have a seat.  My name\'s Orsik')
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
  
    if msg.channel == chnl:
        await bot.send_message(chnl, 'Hello, I am Orsik')
    
    elif msg.content.startswith(str(bot.user)):
        await bot.send_message(msg.channel, 'Sorry, but I am an in-character Bot, please join {0.place}').format(chnl)
    return

@bot.command(pass_context=True)
async def check(ctx):
    await bot.say("I am connected!")
    return

async def close(ctx):
    await bot.say("Closing up for the night")
    await bot.close()
    print("Orsik Bot has closed down")
    return

@bot.event
async def on_ready():
    print("Orsik is behind the bar.")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    #Indicate how to interact
    await bot.change_presence(game=discord.Game(name='Call by name'))
    return

bot.run(token) #Token


greetings = ["Hello", "Hi", "Hey", "Good Day"]

nr_actions = ["_is cleaning out a recently finished tankard._",
              "_wipes down the bar._", "_seems to be in deep thought._"]

inns = [("Old Hold",  "Lower City", "near the Gate", "Dwarfs", ""),
        ("Blushing Mermaid", "Lower City", "northeast", "shady"),
        ("Blade and Stars", "Lower City", "southeast", "comfortable", ),
        ("Helm and Cloak", "Upper City", "northwest", "luxury", "expensive"),
        ("Splurging Sturgeon", "Lower City", "northeast", "good",  "cheap" )
        ("Purple Wyrm Inn and Tavern","Lower City", "central", "quality", "what you would expect")
        ("Three Old Kegs", "Upper City", "east wall of the Ducal Palace", "excellent", "good")]

taverns = [("Elfsong Tavern", "Lower City", "southeast", "quality, but haunting", "bit pricy")]

drinks = ["Mithral Ale", "Local Ale", "Meade"]



