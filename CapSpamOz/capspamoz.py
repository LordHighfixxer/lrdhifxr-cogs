import discord
import re

__author__ = "ScarletRav3n"


class CapSpamOz:
    """Prevent spamming in caps"""

    def __init__(self, bot):
        self.bot = bot
        self.count = 0

    async def on_message(self, m):
        pattern = re.compile(r'''(?x)(\b
            [A-Z](\S*?)[ ]
            [A-Z](\S*?)[ ]
            [A-Z](\S*?)[ ]
            [A-Z](\S*?)
            \b)''')

        def c(s): return [u[0] for u in re.findall(pattern, s)]
        trigger = str(c(m.content))
        for x in self.bot.settings.get_prefixes(m.server):
            if m.content.startswith(x) or m.content.startswith('"') or m.content.startswith('\\'):
                return
            if m.author.bot is False and trigger != "[]":
                self.count += 1
                if self.count > 2:
                    trigger = str(m.author.name) + ' wrote *"' + trigger[2:-2] + '..."*'
                    await self.bot.send_message(m.channel, trigger + "\nLook jackass tone it the fuck down and take your ALL CAPS glory to the salt channel")
                    try:
                        await self.bot.delete_message(m)
                    except discord.errors.Forbidden:
                        await self.bot.send_message(m.channel,
                                                    "(Wanted to delete mid {} but no permissions)".format(m.id))
                    self.count = 0


def setup(bot):
    n = CapSpamOz(bot)
    bot.add_cog(n)
