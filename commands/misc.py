import discord
from os import listdir
from os.path import isfile, join
from discord.ext import commands

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.channel.send("Github : https://github.com/NEXOmega/bot-pes-descartes")

    @commands.command(help="Show the ping of the bot")
    async def ping(self, ctx):
        await ctx.channel.send("Pong !")

    @commands.command(help="Get help on tp; $tp list (tp), $tp get (td) (exo)")
    async def tp(self, ctx, *args):
        if(args[0]=="list"):
            mypath = f"./data/tds/td{args[1]}"
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            files = ", ".join(onlyfiles)
            await ctx.channel.send(f"Nous avons les td :  {files}")
        if(args[0]=="get"):
            mypath = f"./data/tds/td{args[1]}/exo{args[2]}.py"
            with open(mypath) as f:
                contents = f.read()
                await ctx.channel.send(f"```python\n {contents} \n```")


def setup(bot):
    bot.add_cog(MiscCog(bot))
