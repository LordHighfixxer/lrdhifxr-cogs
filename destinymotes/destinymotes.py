from discord.ext import commands
from __main__ import send_cmd_help

class Destinymotes:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/destinymotes/images/'
	
    @commands.group(pass_context=True, pm=True, name='dmote')
    async def _dmote(self, context):
        """Calls Destiny Emotes"""
        if context.invoked_subcommand is None:
            await send_cmd_help(context)
	
    @_dmote.command(pass_context=True, name='zpalm', aliases=['zavala_facepalm'])
    async def _zavala_faceplam(self, context):
        await self.bot.send_file(context.message.channel, '{}zavala_facepalm.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='akiss', aliases=['amanda_kiss'])
    async def _amanda_kiss(self, context):
        await self.bot.send_file(context.message.channel, '{}amanda_kiss.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='axetitan', aliases=['titanaxe'])
    async def _axetitan(self, context):
        await self.bot.send_file(context.message.channel, '{}axetitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='babycrota', aliases=['crotababy'])
    async def _babycrota(self, context):
        await self.bot.send_file(context.message.channel, '{}babycrota.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='banshee', aliases=['gunsmith'])
    async def _banshee(self, context):
        await self.bot.send_file(context.message.channel, '{}banshee.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='cayde', aliases=['cayde6'])
    async def _cayde(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='slycade', aliases=['cayde_sneaky'])
    async def _slycade(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde_sneaky.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='c6thumbs', aliases=['cayde_thumbsup'])
    async def _c6thumbs(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde_thumbsup.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='cayde2', aliases=['cayde62'])
    async def _cayde2(self, context):
        await self.bot.send_file(context.message.channel, '{}cayde2.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='crotatitan', aliases=['titancrota'])
    async def _crotatitan(self, context):
        await self.bot.send_file(context.message.channel, '{}crotatitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='dbtitan', aliases=['darkbladetitan'])
    async def _dbtitan(self, context):
        await self.bot.send_file(context.message.channel, '{}darkbladetitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='eris', aliases=['lilmissmoans'])
    async def _eris(self, context):
        await self.bot.send_file(context.message.channel, '{}eris.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='fallen', aliases=['vandal'])
    async def _fallen(self, context):
        await self.bot.send_file(context.message.channel, '{}fallenvandal.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='titanbook', aliases=['fenchurch'])
    async def _titanbook(self, context):
        await self.bot.send_file(context.message.channel, '{}fenchurch.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='ghost', aliases=['gh'])
    async def _ghost(self, context):
        await self.bot.send_file(context.message.channel, '{}ghost.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='ghost2', aliases=['gh2'])
    async def _ghost2(self, context):
        await self.bot.send_file(context.message.channel, '{}ghost2.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='gdown', aliases=['guardian_down'])
    async def _gdown(self, context):
        await self.bot.send_file(context.message.channel, '{}guardian_down.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='gtaunt', aliases=['guardian_taunt'])
    async def _gtaunt(self, context):
        await self.bot.send_file(context.message.channel, '{}guardian_taunt.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='gunbro', aliases=['thunter'])
    async def _gunbro(self, context):
        await self.bot.send_file(context.message.channel, '{}gunbro.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='hammerbro', aliases=['hammertitan'])
    async def _hammerbro(self, context):
        await self.bot.send_file(context.message.channel, '{}hammerbro.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='huntersword', aliases=['hsword'])
    async def _huntersword(self, context):
        await self.bot.send_file(context.message.channel, '{}huntersword.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='ibtitan', aliases=['bannertitan'])
    async def _ibtitan(self, context):
        await self.bot.send_file(context.message.channel, '{}ibtitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='ikbook', aliases=['ikora_book'])
    async def _ikbook(self, context):
        await self.bot.send_file(context.message.channel, '{}ikora_book.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='iktaunt', aliases=['ikora_taunt'])
    async def _iktaunt(self, context):
        await self.bot.send_file(context.message.channel, '{}ikora_taunt.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='jujulock', aliases=['warlockjuju'])
    async def _jujulock(self, context):
        await self.bot.send_file(context.message.channel, '{}jujulock.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='lastword', aliases=['shin'])
    async def _lastword(self, context):
        await self.bot.send_file(context.message.channel, '{}lastword.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='marasov', aliases=['queen'])
    async def _marasov(self, context):
        await self.bot.send_file(context.message.channel, '{}marasov.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='petra', aliases=['petrareef'])
    async def _petra(self, context):
        await self.bot.send_file(context.message.channel, '{}petra.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='rahool', aliases=['egrampile'])
    async def _rahool(self, context):
        await self.bot.send_file(context.message.channel, '{}rahool.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='trollhool', aliases=['rahooltroll'])
    async def _trollhool(self, context):
        await self.bot.send_file(context.message.channel, '{}rahooltroll.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='razetitan', aliases=['razelighter'])
    async def _razetitan(self, context):
        await self.bot.send_file(context.message.channel, '{}razetitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='saint14', aliases=['st14'])
    async def _saint14(self, context):
        await self.bot.send_file(context.message.channel, '{}saint14.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='saladin', aliases=['saladinforge'])
    async def _saladin(self, context):
        await self.bot.send_file(context.message.channel, '{}saladin.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='nono', aliases=['saladin_no_no'])
    async def _nono(self, context):
        await self.bot.send_file(context.message.channel, '{}saladin_no_no.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='amazing', aliases=['shaxx_amazing'])
    async def _amazing(self, context):
        await self.bot.send_file(context.message.channel, '{}shaxx_amazing.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='haha', aliases=['shaxx_laugh'])
    async def _haha(self, context):
        await self.bot.send_file(context.message.channel, '{}shaxx_laugh.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='sivahunter', aliases=['sivah'])
    async def _sivahunter(self, context):
        await self.bot.send_file(context.message.channel, '{}sivahunter.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='sleeper', aliases=['sleeperlock'])
    async def _sleeper(self, context):
        await self.bot.send_file(context.message.channel, '{}sleeperlock.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='sniper', aliases=['sniperlock'])
    async def _sniper(self, context):
        await self.bot.send_file(context.message.channel, '{}sniperlock.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='hammerbro2', aliases=['hammertitan2'])
    async def _hammerbro2(self, context):
        await self.bot.send_file(context.message.channel, '{}hammerbro2.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='sparrow', aliases=['tricky'])
    async def _sparrow(self, context):
        await self.bot.send_file(context.message.channel, '{}sparrow.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='stalker', aliases=['tether'])
    async def _stalker(self, context):
        await self.bot.send_file(context.message.channel, '{}stalker.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='thorn', aliases=['yor'])
    async def _thorn(self, context):
        await self.bot.send_file(context.message.channel, '{}thorn.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='treasure', aliases=['chest'])
    async def _treasure(self, context):
        await self.bot.send_file(context.message.channel, '{}treasure.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='trialshunter', aliases=['trialsh'])
    async def _trialshunter(self, context):
        await self.bot.send_file(context.message.channel, '{}trialshunter.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='razetitant', aliases=['trialsibrazetitan'])
    async def _razetitant(self, context):
        await self.bot.send_file(context.message.channel, '{}trialsibrazetitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='triumphtitan', aliases=['goldtitan'])
    async def _triumphtitan(self, context):
        await self.bot.send_file(context.message.channel, '{}triumphtitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='thumbdown', aliases=['uldren_taunt'])
    async def _thumbdown(self, context):
        await self.bot.send_file(context.message.channel, '{}uldren_taunt'.format(self.base))
	
    @_dmote.command(pass_context=True, name='nooo', aliases=['uldren_nooo'])
    async def _nooo(self, context):
        await self.bot.send_file(context.message.channel, '{}uldren_nooo.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='variks', aliases=['jedgement'])
    async def _variks(self, context):
        await self.bot.send_file(context.message.channel, '{}variks.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='hi', aliases=['variks_greetings'])
    async def _hi(self, context):
        await self.bot.send_file(context.message.channel, '{}variks_greetings.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='vogtitan', aliases=['titanvog'])
    async def _vogtitan(self, context):
        await self.bot.send_file(context.message.channel, '{}vogtitan.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='xur', aliases=['emmisary'])
    async def _xur(self, context):
        await self.bot.send_file(context.message.channel, '{}xur.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='xursday', aliases=['coins'])
    async def _xursday(self, context):
        await self.bot.send_file(context.message.channel, '{}xursday.png'.format(self.base))
	
    @_dmote.command(pass_context=True, name='crochet', aliases=['zavala_scarf'])
    async def _crochet(self, context):
        await self.bot.send_file(context.message.channel, '{}zavala_scarf.png'.format(self.base))
	
def setup(bot):
    n = Destinymotes(bot)
    bot.add_cog(n)
