#!/usr/bin/env python3
import json

import discord
from discord.ext import commands

import music

bot = commands.Bot(command_prefix='//', description="Tha Illest MC")


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name='//help')
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user.name}')
    bot.add_cog(music.Music(bot))


def main():
    with open('../env/config.json') as fh:
        bot.config = json.load(fh)
    bot.run(bot.config['TOKEN'])


if __name__ == "__main__":
    main()
