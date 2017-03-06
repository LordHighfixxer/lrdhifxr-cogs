import discord
from discord.ext import commands
from random import choice


class kessel:
    "kessel kessel"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, aliases=["kessel"])
    async def Kessel(self):
        """Displays a random kessel."""

        # TODO make bigger list
        kessel = ["http://i.imgur.com/HpXZPZ1.gifv",
               "http://i.imgur.com/KsCh67n.gifv",
               "http://i.imgur.com/HIZfEpX.gifv",
               "http://i.imgur.com/uzubEP8.gifv",
               "http://i.imgur.com/SRQYQjy.jpg",
               "http://i.imgur.com/clPnnul.gifv",
               "http://i.imgur.com/yXgXd4W.gifv"]

        kessel = choice(kessel)

        kesselsay = ["kessel!!11", "Kessel Intensification Protocol Engaged", "Neeeeeeeeeeeeeeeeeeeeeeepppppppppp",
                  "kessel kessel :P", "*intense kesseling*", "I ran out of Kessel so here is some more"]
        kesselsay = choice(kesselsay)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description="", colour=discord.Colour(value=colour))
        data.add_field(name=kesselsay, value=u"\u2063")
        data.set_image(url=kessel)

        try:
            await self.bot.say(embed=data)
        except:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")


def setup(bot):
bot.add_cog(kessel(bot))