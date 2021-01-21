import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix=os.getenv("PREFIX"))

@bot.command(help="Show the ping of the bot")
async def ping(ctx):
    await ctx.channel.send("Pong !")

@bot.command(help="Ecris un message de façon animée")
async def animate(ctx, *args):
    await ctx.message.delete()
    message = await ctx.channel.send(args[0])
    for x in range(1, len(args)):
        await asyncio.sleep(1)
        await message.edit(content=args[x])

@bot.command(help="Fais dire un message au bot")
async def tell(ctx, *args):
    await ctx.message.delete()
    await ctx.channel.send(" ".join(args))

bot.run(DISCORD_TOKEN)