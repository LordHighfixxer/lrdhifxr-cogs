import os
import discord
from discord.ext import commands
from .utils.dataIO import dataIO


class STREAMCON:

    """Server STREAMCON Levels"""

    def __init__(self, bot):
        self.bot = bot
        self.settings_path = "data/STREAMCON/settings.json"
        self.settings = dataIO.load_json(self.settings_path)
        self.valid_STREAMCONs = ['1', '2', '3', '4', '5']

    @commands.command(name="STREAMCON", no_pm=True, pass_context=True)
    async def STREAMCON(self, ctx):
        """Reports the server STREAMCON level."""
        server = ctx.message.server
        self.load_settings(server)
        nick = self.settings[server.id]["authority"]
        await self.post_STREAMCON(str(self.settings[server.id]["STREAMCON"]), nick)

    @commands.command(name="STREAMCON+", no_pm=True, pass_context=True)
    async def STREAMCONplus(self, ctx):
        """Elevates the server STREAMCON level."""
        server = ctx.message.server
        member = ctx.message.author
        self.load_settings(server)
        if self.settings[server.id]["STREAMCON"] == 1:
            await self.bot.say("We are already at STREAMCON 1! Oh no!")
        else:
            self.settings[server.id]["STREAMCON"] -= 1

        self.settings[server.id]["authority"] = member.display_name
        self.save_settings(server)
        await self.post_STREAMCON(str(self.settings[server.id]["STREAMCON"]),
                               member.display_name)

    @commands.command(name="STREAMCON-", no_pm=True, pass_context=True)
    async def STREAMCONminus(self, ctx):
        """Lowers the server STREAMCON level."""
        server = ctx.message.server
        member = ctx.message.author
        self.load_settings(server)
        if self.settings[server.id]["STREAMCON"] == 5:
            await self.bot.say("We are already at STREAMCON 5! Relax!")
        else:
            self.settings[server.id]["STREAMCON"] += 1

        self.settings[server.id]["authority"] = member.display_name
        self.save_settings(server)
        await self.post_STREAMCON(str(self.settings[server.id]["STREAMCON"]),
                               member.display_name)

    @commands.command(name="setSTREAMCON", no_pm=True, pass_context=True)
    async def setSTREAMCON(self, ctx, level):
        """Manually set the server STREAMCON level in case of emergency."""
        server = ctx.message.server
        member = ctx.message.author
        self.load_settings(server)

        if level in self.valid_STREAMCONs:
            self.settings[server.id]["STREAMCON"] = int(level)
            self.settings[server.id]["Authority"] = member.display_name
            self.save_settings(server)
            await self.post_STREAMCON(str(self.settings[server.id]["STREAMCON"]),
                                   member.display_name)
        else:
            await self.bot.say("Not a valid STREAMCON level. Haven't "
                               "you seen War Games Guardian?")

    async def post_STREAMCON(self, level, nick):

        icon_url = 'http://i.imgur.com/MfDcOEU.gif'

        if level == '5':
            color = 0x0080ff
            thumbnail_url = 'http://i.imgur.com/uTPeW7N.gif'
            author = "This outpost is at STREAMCON LEVEL {}.".format(level)
            subtitle = ("No known darkness induced NaCl related threats "
                        "exist at this time.")
            instructions = ("- Partipaction in Crucible matches is encouraged\n"
                            "- Remain vigilant of Guardian trolls\n"
			    "- Think about saying nice things to Master Rahool\n"
                            "- Report all suspicious activity by Cayde-6")
        elif level == '4':
            color = 0x00ff00
            thumbnail_url = 'http://i.imgur.com/siIWL5V.gif'
            author = "This outpost is at STREAMCON LEVEL {}.".format(level)
            subtitle = 'Trace amounts of sodium have been detected.'
            instructions = ("- Inhale deeply through your nose and "
                            "count to 5\n"
                            "- Take short breaks between missions\n"
			    "- Avoid allowing Trials unless well rested\n"
                            "- Do not encourage Warlocks to attempt jump puzzles")
        elif level == '3':
            color = 0xffff00
            thumbnail_url = 'http://i.imgur.com/E71VSBE.gif'
            author = "This outpost is at STREAMCON LEVEL {}.".format(level)
            subtitle = 'Sodium levels may exceed Tower exposure limits.'
            instructions = ("- Use extreme caution when playing Crucible matches\n"
                            "- Log off non-essential communication channels\n"
			    "- Stay out of Trials of Osiris\n"
                            "- Put on your big boy pants")
        elif level == '2':
            color = 0xff0000
            thumbnail_url = 'http://i.imgur.com/PxKhT7h.gif'
            author = "This outpost is at STREAMCON LEVEL {}.".format(level)
            subtitle = 'Sodium levels are approaching critical mass'
            instructions = ("- Avoid Nightfall at all costs\n"
                            "- Mute all hostile voice channels\n"
			    "- Call Hideo's mom and tell her you love her\n"
			    "- Start stashing your favorite gear away\n"
                            "- Queue up some relaxing Radiohead music")
        elif level == '1':
            color = 0xffffff
            thumbnail_url = 'http://i.imgur.com/wzXSNWi.gif'
            author = "This outpost is at STREAMCON LEVEL {}.".format(level)
            subtitle = 'The Darkness is upon us; destruction IMMINENT.'
            instructions = ("- Do not participate in any Crucible game modes\n"
                            "- Avoid speaking to the anyone in charge\n"
                            "- Evacuate the outpost until the "
                            "all-clear is given")

        if level in self.valid_STREAMCONs:
            embed = discord.Embed(title="\u2063", color=color)
            embed.set_author(name=author, icon_url=icon_url)
            embed.set_thumbnail(url=thumbnail_url)
            embed.add_field(name=subtitle, value=instructions, inline=False)
            embed.set_footer(text="Authority: {}".format(nick))
            await self.bot.say(embed=embed)
        else:
            await self.bot.say("There was an error due to Vex interference Guardian.")

    def load_settings(self, server):
        self.settings = dataIO.load_json(self.settings_path)
        if server.id not in self.settings.keys():
            self.add_default_settings(server)

    def save_settings(self, server):
        if server.id not in self.settings.keys():
            self.add_default_settings(server)
        dataIO.save_json(self.settings_path, self.settings)

    def add_default_settings(self, server):
        self.settings[server.id] = {"STREAMCON": 5, "authority": "none"}
        dataIO.save_json(self.settings_path, self.settings)


def check_folders():
    folder = "data/STREAMCON"
    if not os.path.exists(folder):
        print("Creating {} folder...".format(folder))
        os.makedirs(folder)


def check_files():
    default = {}
    if not dataIO.is_valid_json("data/STREAMCON/settings.json"):
        print("Creating default STREAMCON settings.json...")
        dataIO.save_json("data/STREAMCON/settings.json", default)


def setup(bot):
    check_folders()
    check_files()
    n = STREAMCON(bot)
    bot.add_cog(n)
