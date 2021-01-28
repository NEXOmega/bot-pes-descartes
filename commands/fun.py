import discord
from discord.ext import commands
import asyncio

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Ecris un message de façon animée")
    async def animate(self, ctx, *args):
        await ctx.message.delete()
        message = await ctx.channel.send(args[0])
        for x in range(1, len(args)):
            await asyncio.sleep(1)
            await message.edit(content=args[x])

    @commands.command(help="Fais dire un message au bot")
    async def tell(self, ctx, *args):
        await ctx.message.delete()
        await ctx.channel.send(" ".join(args))

def setup(bot):
    bot.add_cog(FunCog(bot))
