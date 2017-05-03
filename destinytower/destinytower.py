import discord
from discord.ext import commands
from random import choice


class destinytower:
    "Delivers a Random Destiny Tower PA Quote"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, aliases=["destinytower"])
    async def destinytower(self):
        """Displays a random Quote from Destinys Tower PA."""

        # TODO make bigger list
        destinytower = ["http://i.imgur.com/HpXZPZ1.gif",
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
        destinytower = choice(destinytower)

        destinytowersay = ["destinytower!!11", "destinytower Intensification Protocol Engaged", "Keeeeeeesssssssel",
                  "destinytower destinytower :P", "*intense destinytowering*", "I ran out of destinytower so here is some more"]
        destinytowersay = choice(destinytowersay)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description="", colour=discord.Colour(value=colour))
        data.add_field(name=destinytowersay, value=u"\u2063")
        data.set_image(url=destinytower)

        try:
            await self.bot.say(embed=data)
        except:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")


def setup(bot):
     bot.add_cog(destinytower(bot))
