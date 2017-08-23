#rebuild version of orsik

import discord
from discord.ext import commands
import asyncio

with open("orsiktoken") as f:
    for line in f:
        token=str(line)

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        print('No talking to yourself')
        return

    if message.content.startswith('$channel'):
    	print('Channel is '+str(message.channel))
    	await client.send_message(message.channel, 'Channel is '+str(message.channel))

    if message.content.startswith('$guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 10')
        
        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.send_message('general', 'Connected')

client.run(token)