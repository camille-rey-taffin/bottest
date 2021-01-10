# bot.py
import os
import re
import discord
import csv
from dotenv import load_dotenv
from questions import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#DISCORD_GUILD=os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):

    if message.author==client.user:
        return

    if message.author.bot:
        return

    if re.match(r'^!', message.content):
        requete = to_requete(message)
        await message.channel.send(type(requete))
client.run(TOKEN)
