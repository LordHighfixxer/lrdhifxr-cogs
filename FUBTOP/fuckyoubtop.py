import discord
from discord.ext import commands
from random import choice as randchoice

class Fuck:
    """Display fuck you statements"""

    def __init__(self, bot):
        self.bot = bot
        self.fuck = ["You mean nothing to me without wings in your hands {}! ~{}","Fuck you, {}. ~{}", "Fucking fuck off, {}. ~{}","Fuck off, {}. ~{}","Fuck this, {}. ~{}", "Fuck that, {}. ~{}","Eat a dick, {}. ~{}"]

    @commands.command(pass_context=True, no_pm=True)
    async def fuckyou(self, ctx, user : discord.Member=None):
        """Get fuck you statements"""
        
        auth = ctx.message.author
        if not user:
            data = discord.Embed(colour=auth.colour)
            data.add_field(name="Error:warning:",value="You have to mention a user, {}".format(auth.mention))
            await self.bot.say(embed=data)
        else:
            fuck = randchoice(self.fuck).format(user.mention, auth.mention)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Fuck You!:CmonDawg:",value="{}".format(fuck))
            await self.bot.say(embed=data)

def setup(bot):
bot.add_cog(Fuck(bot))