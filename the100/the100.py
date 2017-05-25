from discord.ext import commands
import aiohttp
import requests

class The100:
    """Group Information From the100.io"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def the100(self):
        """Gets a the100 information."""
        headers = {
			'Authorization': 'Token token="hLeSA0v7Hahke71qp1Hs2Q"',
		}
        requests.get('https://www.the100.io/api/v1//groups/4311/gaming_sessions', headers=headers) as r:
		result = await r.text()
		await self.bot.say('`' + result + '`')


def setup(bot):
    n = The100(bot)
    bot.add_cog(n)
