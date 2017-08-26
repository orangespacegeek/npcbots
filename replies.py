import discord
from discord.ext import commands
import random
import asyncio
from textblob import TextBlob

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
     
    if message.content.startswith('Greetings'):
        await client.send_message(message.channel, 'Greetings? Why not say "hello" like a normal person?')
        msg = await client.wait_for_message(author=message.author, content='hello')
        await client.send_message(message.channel, 'Hello.')

    if message.content.startswith('Hireling, hold'):
        msg = 'Yes, Master. *takes item from {0.author.display_name} and puts it in his pack.*'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Hireling, give'):
        msg = 'Right away! *takes item out of pack and hands it to {0.author.display_name}*'.format(message)
        await client.send_message(message.channel, msg)
                   
    if message.content.startswith('Good'):
        msg = "*mumbles* What's so good about it?".format(message)
        await client.send_message(message.channel, msg)
        return


client.run('MzQ5NzMxODI3NTYyNDQ2ODQ5.DIEorA.Sm9KDiiUw_6x81hr387TV7Pf8Q0')
