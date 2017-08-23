#Orsik, Dwarf male, operator of the Empty Tankard


#Client ID 349695599186280448

#To add to a server, https://discordapp.com/oauth2/authorize?client_id=349695599186280448&scope=bot&permissions=0

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()


bot_prefix= "Orsik, "
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Orsik is behind the bar.")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Indicate how to interact
    await client.change_presence(game=discord.Game(name='Call by name'))
    await client.send_message(message.channel, 'Hi, I am Orsik')

async def on_member_join(member):
	await client.send_message(message.channel, 'Welcome to the Empty Tankard, have a sit.  My name\'s Orsik')

@client.command(pass_context=True)
async def ale(ctx):
    await client.say("_fills an empty tankard and puts it on the bar._")
    await client.say("That will be two copper.")

client.run("MzQ5Njk1NTk5MTg2MjgwNDQ4.DH5O_Q.cF4RWm-WHNZA57S_VVNxxfGobUw") #Token

#
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



