from discord.ext import commands


class Detinymotes:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/memes/images/'
	
    @commands.group(pass_context=True, no_pm=True, name='dmote')
    async def _dmote(self, context):
        """Calls Destiny Emotes"""
        if context.invoked_subcommand is None:
		await send_cmd_help(context)

    @dmote.command(pass_context=True, aliases=;['zpalm'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}zavala_facepalm.png'.format(self.base))

    @dmote.command(pass_context=True, aliases=['tflip'])
    async def _xursday(self, context):
        await self.bot.send_file(context.message.channel, '{}xursday.png'.format(self.base))
    
def setup(bot):
    n = Destinymotes(bot)
    bot.add_cog(n)
