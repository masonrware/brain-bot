import discord
from discord.ext import commands, tasks
import youtube_dl

from random import choice

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print('brainBot is now online!')


client.run('OTI5MjQ2NTYwOTkzMzEyODYw.YdkiTA.b8nSqb6MTnt3oJQ5n615ufVFgiY')
