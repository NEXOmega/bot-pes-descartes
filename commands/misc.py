import discord
from discord.ext import commands

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command()
    async def info(self, ctx):
        await ctx.channel.send("Github : ")

    @commands.command(help="Show the ping of the bot")
    async def ping(self, ctx):
        await ctx.channel.send("Pong !")

def setup(bot):
    bot.add_cog(MiscCog(bot))