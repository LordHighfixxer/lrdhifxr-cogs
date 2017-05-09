import aiohttp
from discord.ext import commands


class Dadjoke():
    """A cog for getting dad jokes"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=True, name="dadjoke")
    async def _dadjoke(self, ctx):
        """Gets a random cat fact"""
        async with aiohttp.get("https://icanhazdadjoke.com/") as cfget:
            fact_json = accept application/json()
        fact = fact_json["facts"][0]
        await self.bot.say("Ok " + ctx.message.author.mention + ", here is a dad joke.\n" + fact)



def setup(bot):
    n = Dadjoke(bot)
    bot.add_cog(n)
