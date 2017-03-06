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
        kessel = ["http://i.imgur.com/HpXZPZ1.gif",
               "http://i.imgur.com/KsCh67n.gif",
               "http://i.imgur.com/HIZfEpX.gif",
               "http://i.imgur.com/uzubEP8.gif",
               "http://i.imgur.com/SRQYQjy.jpg",
               "http://i.imgur.com/clPnnul.gif",
               "http://i.imgur.com/k6JwlGp.jpg",
               "http://i.imgur.com/3ihp9Gl.gif",                  
               "http://i.imgur.com/EAWFfAZ.jpg",                  
               "http://i.imgur.com/uBywNQO.jpg", 
               "http://i.imgur.com/voBmkuO.gif",                   
               "http://i.imgur.com/r1gl4Nl.jpg",                  
               "http://i.imgur.com/BKrcNTs.jpg",                  
               "http://i.imgur.com/GskTVj0.gif",
               "http://i.imgur.com/pKQCbDO.gif",                  
               "http://i.imgur.com/yXgXd4W.gif"]

        kessel = choice(kessel)

        kesselsay = ["kessel!!11", "Kessel Intensification Protocol Engaged", "Keeeeeeesssssssel",
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
