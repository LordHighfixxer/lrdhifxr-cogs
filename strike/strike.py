from __main__ import send_cmd_help
from .utils.dataIO import dataIO
from discord.ext import commands
from .utils import checks
import datetime
import asyncio
import discord
import random
import time
import os


class strike:
    def __init__(self, bot):
        self.bot = bot
        self.scores = dataIO.load_json('data/strike/scores.json')
        self.subscriptions = dataIO.load_json('data/strike/subscriptions.json')
        self.settings = dataIO.load_json('data/strike/settings.json')
        self.animals = {'Fallen': ':imp:', 'Hive': ':jack_o_lantern:', 'Vex': ':robot:', 'Cabal': ':turtle:', 'Splicer': ':japanese_ogre:'}
        self.in_game = []
        self.paused_games = []
        self._latest_message_check_message_limit = 5
        self._latest_message_check_wait_limit = self.settings['strike_interval_maximum'] * 2
        self.next = None

    async def _save_scores(self):
        dataIO.save_json('data/strike/scores.json', self.scores)

    async def _save_subscriptions(self):
        dataIO.save_json('data/strike/subscriptions.json', self.subscriptions)

    async def _save_settings(self):
        dataIO.save_json('data/strike/settings.json', self.settings)

    @commands.group(pass_context=True, no_pm=True, name='strike')
    async def _strike(self, context):
        """Vanguard Strikes against the minions of The Darkness"""
        if context.invoked_subcommand is None:
            await send_cmd_help(context)

    @_strike.command(pass_context=True, no_pm=True, name='start')
    async def _start(self, context):
        """Begin the Strike mission"""
        server = context.message.server
        channel = context.message.channel
        if server.id in self.subscriptions:
            message = '**Guardian we\'re already on a strike!**'
        else:
            self.subscriptions[server.id] = channel.id
            message = '**The go order from the Vanguard has beeen received. Eyes Up Guardians.**'
            await self._save_subscriptions()
        await self.bot.say(message)

    @_strike.command(pass_context=True, no_pm=True, name='stop')
    async def _stop(self, context):
        """Stop the Strike"""
        server = context.message.server
        if server.id not in self.subscriptions:
            message = '**Guardian we\'re not on a strike!**'
        else:
            del self.subscriptions[server.id]
            message = '**The Strike has stopped Guardian.**'
            await self._save_subscriptions()
        await self.bot.say(message)

    @_strike.command(no_pm=True, name='timing')
    @checks.is_owner()
    async def _timing(self, interval_min: int, interval_max: int, bang_timeout: int):
        """Change the timing for Strikes"""
        if interval_min > interval_max:
            message = '**`interval_min` needs to be lower than `interval_max`**'
        elif interval_min < 0 and interval_max < 0 and bang_timeout < 0:
            message = '**Please no negative numbers!**'
        else:
            self.settings['strike_interval_minimum'] = interval_min
            self.settings['strike_interval_maximum'] = interval_max
            self.settings['wait_for_bang_timeout'] = bang_timeout
            await self._save_settings()
            message = '**Timing has been set.**'
        await self.bot.say(message)

    @_strike.command(no_pm=True, name='next')
    @checks.is_owner()
    async def _next(self):
        """When will the next Strike happen?"""
        if self.next:
            message = '**Guardian, the next occurance will be at {} UTC**'.format(self.next)
        else:
            message = '**There is currently no Strike in the planning phase Guardian.**'
        await self.bot.say(message)

    @_strike.command(pass_context=True, no_pm=True, name='score')
    async def _score(self, context, member: discord.Member):
        """This will show the score of a Guardian"""
        server = context.message.server
        if server.id in self.scores:
            if member.id in self.scores[server.id]:
                message = '**{} shot a total of {} minions of the darkness ({})**'.format(member.mention, self.scores[server.id][member.id]['total'], ', '.join([str(self.scores[server.id][member.id][x]) + ' ' + x.capitalize() + 's' for x in self.scores[server.id][member.id] if x != 'total']))
            else:
                message = '**Guardian, please shoot something on a Strike before you try to brag about it.  Try not to be like Cayde-6**'
        else:
            message = '**Guardian, please shoot something on a Strike before you try to brag about it.  Try not to be like Cayde-6**'
        await self.bot.say(message)

    @_strike.command(pass_context=True, no_pm=True, name='leaderboard', aliases=['scores'])
    async def _strikeboard(self, context):
        """This will show the top Guardian Strike scores on this server"""
        server = context.message.server
        if server.id in self.scores:
            p = self.scores[server.id]
            scores = sorted(p, key=lambda x: (p[x]['total']), reverse=True)
            message = '```\n{:<4}{:<8}{}\n\n'.format('#', 'TOTAL', 'USERNAME')
            for i, hunter in enumerate(scores, 1):
                if i > 20:
                    break
                message += '{:<4}{:<8}{} ({})\n'.format(i, p[hunter]['total'], p[hunter]['author_name'], ', '.join([str(p[hunter]['score'][x]) + ' ' + x.capitalize() + 's' for x in p[hunter]['score']]))
            message += '```'
        else:
            message = '**Guardian, please shoot something on a Strike before you try to brag about it.  Try not to be like Cayde-6**'
        await self.bot.say(message)

    async def add_score(self, server, author, avian):
        if server.id not in self.scores:
            self.scores[server.id] = {}
        if author.id not in self.scores[server.id]:
            self.scores[server.id][author.id] = {}
            self.scores[server.id][author.id]['score'] = {}
            self.scores[server.id][author.id]['total'] = 0
            self.scores[server.id][author.id]['author_name'] = ''
            for a in list(self.animals.keys()):
                self.scores[server.id][author.id]['score'][a] = 0
        if avian not in self.scores[server.id][author.id]['score']:
            self.scores[server.id][author.id]['score'][avian] = 0
        self.scores[server.id][author.id]['author_name'] = author.display_name
        self.scores[server.id][author.id]['score'][avian] += 1
        self.scores[server.id][author.id]['total'] += 1
        await self._save_scores()

    async def _wait_for_bang(self, server, channel):
        def check(message):
            return message.content.lower().split()[0] == 'bang' or message.content.lower().split()[0] == 'b'

        animal = random.choice(list(self.animals.keys()))
        await self.bot.send_message(channel, self.animals[animal])
        message = await self.bot.wait_for_message(channel=channel, timeout=self.settings['wait_for_bang_timeout'], check=check)
        if message:
            author = message.author
            if random.randrange(0, 17) > 1:
                await self.add_score(server, author, animal)
                msg = '**{} shot a {}!**'.format(author.mention, animal)
            else:
                msg = '**{} missed the shot and the {} retreated to cal for reinforcements!**'.format(author.mention, animal)
        else:
            msg = '**The {} got away!** :confused:'.format(animal)
        self.in_game.remove(channel.id)
        await self.bot.send_message(channel, msg)

    async def _latest_message_check(self, channel):
        async for message in self.bot.logs_from(channel, limit=self._latest_message_check_message_limit, reverse=True):
            delta = datetime.datetime.utcnow() - message.timestamp
            if delta.total_seconds() < self._latest_message_check_wait_limit and message.author.id != self.bot.user.id:
                if channel.id in self.paused_games:
                    self.paused_games.remove(channel.id)
                return True
        if channel.id not in self.paused_games:
            self.paused_games.append(channel.id)
            await self.bot.send_message(channel, '**It seems there are no Guardians here. The Strike will be resumed when someone treads here again.**')
        return False

    async def _strike_loop(self):
        while self == self.bot.get_cog('strike'):
            wait_time = random.randrange(self.settings['strike_interval_minimum'], self.settings['strike_interval_maximum'])
            self.next = datetime.datetime.fromtimestamp(int(time.mktime(datetime.datetime.utcnow().timetuple())) + wait_time)
            await asyncio.sleep(wait_time)
            for server in self.subscriptions:
                if self.subscriptions[server] not in self.in_game:
                    channel = self.bot.get_channel(self.subscriptions[server])
                    server = self.bot.get_server(server)
                    if await self._latest_message_check(channel):
                        self.in_game.append(self.subscriptions[server.id])
                        self.bot.loop = asyncio.get_event_loop()
                        self.bot.loop.create_task(self._wait_for_bang(server, channel))


def check_folder():
    if not os.path.exists('data/strike'):
        print('Creating data/strike folder...')
        os.makedirs('data/strike')


def check_files():
    f = 'data/strike/settings.json'
    if not dataIO.is_valid_json(f):
        print('Creating empty settings.json...')
        data = {}
        data['strike_interval_minimum'] = 300
        data['strike_interval_maximum'] = 600
        data['wait_for_bang_timeout'] = 30
        dataIO.save_json(f, data)

    f = 'data/strike/subscriptions.json'
    if not dataIO.is_valid_json(f):
        print('Creating empty subscriptions.json...')
        dataIO.save_json(f, {})

    f = 'data/strike/scores.json'
    if not dataIO.is_valid_json(f):
        print('Creating empty scores.json...')
        dataIO.save_json(f, {})


def setup(bot):
    check_folder()
    check_files()
    cog = strike(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(cog._strike_loop())
    bot.add_cog(cog)
