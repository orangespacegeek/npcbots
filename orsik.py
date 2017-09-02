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

#Discord setup functions
bot = discord.Client()

bot_prefix= "O$"

global targetchannel
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
        global targetchannel
        targetchannel = msg.channel
        response = '`Orsik will respond with In-Character messages in {0}`'.format(str(targetchannel))
        print('$targetchannel is {}'.format(targetchannel))
        await bot.send_message(msg.channel, response)
        return

#Trigger for in-character interactions
    elif msg.content.startswith('Orsik') and msg.author != bot.user:
        
        user = msg.author
        name = user.display_name

#formats the statement for further analysis
        statement = msg.content
        if len(statement) < 6:
            statement = msg.content
        elif len(statement) > 5:
            if statement[5] == ",":
                statement = statement[6:]
            else:
                statement = statement[5:]

#If it is not the assigned channel, lets the user know
        if msg.channel != targetchannel:
            response = '`Orsik BOT is assigned to {}`'.format(str(targetchannel))
            await bot.send_message(msg.channel, response)
            return            

#General response to a name
        elif msg.content == 'Orsik':
            ya = random.choice(affirm)
            aid = random.choice(assit)
            response =  '{0} {1}, how can I {2} you?'.format(ya.capitalize(), name.capitalize(), aid)           

#This section is the meat of the bots responses, it is where most of the change will occur

#For questions, targets context and answers the question            
        elif statement.endswith('?'):
            [qtype, target] = question(statement)
            response = expertise(target)

        else:
            response = random.choice(nr_actions)
           
    else:
        return
    
    if targetchannel == 'null':
        await bot.send_message(msg.channel, 'Please assign Orsik to a channel with $targetchannel')
    else:
        await bot.send_message(targetchannel, response)

#@bot.event
#async def on_member_update(old_state,new_state):
#    hello = '{0} to the Empty Tankard, have a seat.  My name\'s Orsik'.format(random(greetings))

#    await bot.send_message(hello)

@bot.command() #not currently working
async def shutter():
    print('Closing connection to server for bot')
    await bot.send_message(targetchannel, "Closing down folks.")
    await bot.close()
    return

@bot.event
async def on_ready():
    print("-------")
    print("Orsik is behind the bar.")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("-------")
    #Indicate how to interact
    global targetchannel
    targetchannel = 'null' #inital setting prior to in-Discord reset
    print('$targetchannel is {}'.format(targetchannel))

    await bot.change_presence(game=discord.Game(name='Behind the bar'))
    

#statement reading/response generating functions
def question(sentence):
    words = sentence.split()
    qtype = words[0]
    word = words[-1:]
    word = word[0]
    word = word[:-1]
    return [qtype, word]

def drink(desired):
    return

def expertise(word):
    #Flint
    if word == 'Flint':
        sentence = random.choice(flint) #says what Orsik thinks of flint

    #Ale
    elif word.lower() == 'ale':
        sentence = random.choice(ale) #offers up some info on ales

    #Inn
    elif word.lower() == 'inn':
        inn = random.choice(inns) #randomly chooses an inn to discuss
        inn = list(inn) #converts tuple to a list
        name= inn[0]
        direction = inn[2]
        quarter = inn[1]
        sentence = "You might try the {0}. It is around the {1} of {2}.".format(name, direction, quarter)
    else:
        sentence = "Sorry, I am not familar.  Perhaps you get a hold of one of Volo's guides."
        #if he doesn't know anything about it, he suggests finding a guide by the famous Volo.

    return sentence


#Source List and Tuples
greetings = ["hello", "hi", "hey", "good day"]

affirm = ["yes", "aye", "ya"]

assit = ["help", "aid", "assist"]

flint = ["Flint? One of the best dwarfs I know.", " True champion of Moradin.", "Saved my life more than once."]

ale = ["I carry Mithral Ale and a local ale, a light blonde.", "Sorry, I do not have the range to be found in the Dwarven Holds of the North.", "No, better beverage."]

nr_actions = ["_is cleaning out a recently finished tankard._",
              "_wipes down the bar._", "_seems to be in deep thought._"]

inns = [("Old Hold",  "Lower City", "Gate", "Dwarfs", ""),
        ("Blushing Mermaid", "Lower City", "northeast area", "shady", ""),
        ("Blade and Stars", "Lower City", "southeast part", "comfortable", "not bad"),
        ("Helm and Cloak", "Upper City", "northwest blocks", "luxury", "expensive"),
        ("Splurging Sturgeon", "Lower City", "northeast part", "good",  "cheap" ),
        ("Purple Wyrm Inn and Tavern","Lower City", "central area", "quality", "what you would expect"),
        ("Three Old Kegs", "Upper City", "east wall of the Ducal Palace", "excellent", "good")]

taverns = [("Elfsong Tavern", "Lower City", "southeast", "quality, but haunting", "bit pricy")]

drinks = ["Mithral Ale", "Local Ale", "Meade"]


token=gettoken("orsiktoken") #Token is stored in a separate file and pulled for the call

bot.run(token) 


