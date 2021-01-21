import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix=os.getenv("PREFIX"))

initial_extensions = ['commands.fun', 'commands.misc']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(os.getenv("DISCORD_TOKEN"))