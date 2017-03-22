import discord
from discord.ext import commands
from random import choice


class cybil:
    "cybil cybil"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, aliases=["cybil"])
    async def cybil(self):
        """Displays a random cybil."""

        # TODO make bigger list
        cybil = ["God you suck at this game Adam.",
               "I could kick your ass at this game Adam.",
               "I do not enjoy people making fun of you.  I enjoy them knowing how terrible you are at life Adam.",
               "Fort says you suck, and you do Adam",
               "Wow, you still suck Adam.",
               "We do not need to buy a vacuum.  You already suck enough Adam.",
               "CAN YOU NOT SEE I AM TRYING TO GET READY FOR WORK ADAM?!?!?!?!"]

        cybil = choice(cybil)

        cybilsay = ["Cybil Intensification Protocol Engaged", "Adam sucks and here is why"]
        cybilsay = choice(cybilsay)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description="", colour=discord.Colour(value=colour))
        data.add_field(name=cybilsay, value=u"\u2063")
        data.set_image(url=cybil)

        try:
            await self.bot.say(embed=data)
        except:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")


def setup(bot):
     bot.add_cog(cybil(bot))
