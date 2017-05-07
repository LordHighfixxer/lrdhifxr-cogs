from discord.ext import commands
from __main__ import send_cmd_help

class Destinymotes:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/destinymotes/images/'
	
    @commands.group(pass_context=True, no_pm=True, name='dmote')
    async def _dmote(self, context):
        """Calls Destiny Emotes"""
        if context.invoked_subcommand is None:
            await send_cmd_help(context)
	
        @_dmote.command(pass_context=True, name='zavala_faceplam', aliases=['zpalm'])
        async def _zavala_faceplam(self, context):
            await self.bot.send_file(context.message.channel, '{}zavala_facepalm.png'.format(self.base))
    
def setup(bot):
    n = Destinymotes(bot)
    bot.add_cog(n)
