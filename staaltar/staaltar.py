import discord
from discord.ext import commands
from random import choice


class staaltar:
    "staaltar staaltar"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, aliases=["staaltar"])
    async def Staaltar(self):
        """Displays a random staaltar."""

        # TODO make bigger list
        staaltar = ["https://i.imgur.com/urvgEdm.jpg",
               "https://i.imgur.com/KJ3mSCf.png",
               "https://i.imgur.com/epWDs2k.png",
               "https://i.imgur.com/Uq223AB.mp4",
               "https://i.imgur.com/SRQYQjy.jpg",
               "https://i.imgur.com/iQ41PLN.png",
               "https://i.imgur.com/hIPJO8M.png"]

        staaltar = choice(staaltar)

        staaltarsay = ["KNEEL BEFORE THE STAALTAR!!!", "Staaltar Adulation Protocol Engaged"]
        staaltarsay = choice(staaltarsay)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description="", colour=discord.Colour(value=colour))
        data.add_field(name=staaltarsay, value=u"\u2063")
        data.set_image(url=staaltar)

        try:
            await self.bot.say(embed=data)
        except:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")


def setup(bot):
    bot.add_cog(staaltar(bot))
