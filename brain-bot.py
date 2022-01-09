import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import youtube_dl

from random import choice

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print('brainBot is now online!')

load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
