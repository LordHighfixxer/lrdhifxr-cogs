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
	
    @_dmote.command(pass_context=True, name='zpalm', aliases=['zavala_facepalm'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}zavala_facepalm.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='akiss', aliases=['amanda_kiss'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}amanda_kiss.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='axetitan', aliases=['titanaxe'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}axetitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='babycrota', aliases=['crotababy'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}babycrota.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='banshee', aliases=['gunsmith'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}banshee.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='cayde', aliases=['cayde6'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='slycade', aliases=['cayde_sneaky'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde_sneaky.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='c6thumbs', aliases=['cayde_thumbsup'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde_thumbsup.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='cayde2', aliases=['cayde62'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde2.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='crotatitan', aliases=['titancrota'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}crotatitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='dbtitan', aliases=['darkbladetitan'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}darkbladetitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='eris', aliases=['lilmissmoans'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}eris.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='fallen', aliases=['vandal'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}fallenvandal.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='titanbook', aliases=['fenchurch'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}fenchurch.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='ghost', aliases=['gh'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}ghost.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='ghost', aliases=['gh2'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}ghost.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='gdown', aliases=['guardian_down'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}guardian_down.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='gtaunt', aliases=['guardian_taunt'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}guardian_taunt.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='gunbro', aliases=['trialshunter'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}gunbro.png'.format(self.base))

def setup(bot):
    n = Destinymotes(bot)
    bot.add_cog(n)
