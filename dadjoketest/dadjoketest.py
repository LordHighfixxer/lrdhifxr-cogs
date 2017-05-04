import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
# Sys
import asyncio
import aiohttp
import time
import random
import os
import sys

class DadJokes:
    """Dad Jokes from icanhazdadjoke.com
    """
    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json(SETTINGS)

    	@commands.group(name="dadjokes", pass_context=True)
	        async def _dadjokes(self, ctx):
		"""Everyone loves a dad joke"""
		if ctx.invoked_subcommand is None:
			await send_cmd_help(ctx)
			return

		# GetDadJoke	
		@commands.command(pass_context=True, no_pm=False)
		async def getdadjoke(self, ctx):
		"""Gets a dad joke."""
			author = ctx.message.author
			try:
				rdm = random.randint(0, self.settings["ama_boobs"])
				search = ("https://icanhazdadjoke.com/j/{}".format(rdm))
				async with aiohttp.get(search) as r:
					result = await r.json()
					joke = random.choice(result)
					joke = "https://icanhazdadjoke.com/j/<id>{}".format(joke["preview"])
			except Exception as e:
				await self.bot.reply("Stop resisting Adam; Error getting results.")
				return
			else:
				await self.bot.send_message(ctx.message.author, "{}".format(joke))  

def check_folders():
        if not os.path.exists(DIR_DATA):
        print("Creating data/dadjokes folder...")
        os.makedirs(DIR_DATA)

def check_files():
        if not os.path.isfile(SETTINGS):
        print("Creating default dadjoke settings.json...")
        dataIO.save_json(SETTINGS, DEFAULT)
        else:  # Key consistency check
        try:
            current = dataIO.load_json(SETTINGS)
        except JSONDecodeError:
            dataIO.save_json(SETTINGS, DEFAULT)
            current = dataIO.load_json(SETTINGS)

        if current.keys() != DEFAULT.keys():
            for key in DEFAULT.keys():
                if key not in current.keys():
                    current[key] = DEFAULT[key]
                    print( "Adding " + str(key) + " field to dadjoke settings.json")
            dataIO.save_json(SETTINGS, DEFAULT)

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(DadJokes(bot))
    bot.loop.create_task(dadjoke.joke_knowlegde())				
