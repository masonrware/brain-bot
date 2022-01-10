import asyncio
import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import youtube_dl


client = commands.Bot(command_prefix='?')




load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
