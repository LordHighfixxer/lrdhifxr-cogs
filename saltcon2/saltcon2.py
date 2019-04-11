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
                               "you seen War Games Doofus?")

    async def post_STREAMCON(self, level, nick):

        icon_url = 'https://i.imgur.com/7psx4VV.gif'

        if level == '5':
            color = 0x0080ff
            thumbnail_url = 'http://i.imgur.com/ap1Es2U.gif'
            author = "Stream status: SCHEDULED HOLD.".format(level)
            subtitle = ("I am either at work or have something scheduled prior to the stream")
            instructions = ("- Expect this status to change later in the day\n"
                            "- Start counting your Tributes\n"
			    "- Stream procedures will continue as planned\n"
                            "- Report all suspicious activity by DJ Woo")
        elif level == '4':
            color = 0x00ff00
            thumbnail_url = 'http://i.imgur.com/UGXYAXn.gif'
            author = "Stream status: GO.".format(level)
            subtitle = 'Stream should launch as scheduled'
            instructions = ("- Strap in and buckle up\n"
                            "- Begin propellant load\n"
			    "- Transfer guidance control to Eddie\n"
			    "- I usually switch to this status once I am out of work\n"
                            "- Stay tuned to Discord or Twitter for updates")
        elif level == '3':
            color = 0xffff00
            thumbnail_url = 'http://i.imgur.com/Oi6VHKw.gif'
            author = "Stream status: HOLD.".format(level)
            subtitle = 'Something has come up but it should be ok.'
            instructions = ("- Stream has a good chance of happening\n"
                            "- This is probably just precautionary\n"
			    "- Expect additional updates\n"
			    "- Feel free to nag me for one too\n"
                            "- Put on your big boy pants")
        elif level == '2':
            color = 0xff0000
            thumbnail_url = 'http://i.imgur.com/34iRGiS.gif'
            author = "Stream status: Engineering HOLD.".format(level)
            subtitle = 'There is a SIGNIFICANT obstacle to streaming'
            instructions = ("- We are pretty sure the stream is not happening\n"
                            "- Queue up something to binge on Netflix\n"
			    "- Check StreamAlerts for who else is live\n"
                            "- Look for additional updates for Go or No-Go")
        elif level == '1':
            color = 0xffffff
            thumbnail_url = 'http://i.imgur.com/mDsJIcd.gif'
            author = "Stream status: SCRUBBED.".format(level)
            subtitle = 'The Stream is POSITIVELY not happening'
            instructions = ("- Stand down from all stream launch plans\n"
                            "- You should absolutely find something else to do\n"
                            "- There will be no further updates.")

        if level in self.valid_STREAMCONs:
            embed = discord.Embed(title="\u2063", color=color)
            embed.set_author(name=author, icon_url=icon_url)
            embed.set_thumbnail(url=thumbnail_url)
            embed.add_field(name=subtitle, value=instructions, inline=False)
            embed.set_footer(text="Authority: {}".format(nick))
            await self.bot.say(embed=embed)
        else:
            await self.bot.say("There was an error due to a downrange tracking system failure.")

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
