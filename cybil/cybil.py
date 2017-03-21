import discord
from discord.ext import commands
from random import choice as randchoice

class Cybilshit:
    """Display Cybil statements"""

    def __init__(self, bot):
        self.bot = bot
        self.cybilshit = ["I could kick your ass at this game Adam","Wow, you suck Adam.","Can you not see I am getting ready for work Adam?","What does don't stick your dick in crazy mean Adam?"]

class Cybil:
    def __init__(self, bot):
        self.bot = bot

    async def listener(self, message):
       auth = member.id == "121246220382502912"
       if 'cybil' in message.content.lower():
            fuck = randchoice(self.cybilshit).format(auth.mention)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Fuck You!",value="{}".format(fuck))
            await self.bot.say(embed=data)
            
def setup(bot):
    n = Cybil(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)
