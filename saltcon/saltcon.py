import os
import discord
from discord.ext import commands
from .utils.dataIO import dataIO


class saltcon:

    """Server saltcon Levels"""

    def __init__(self, bot):
        self.bot = bot
        self.settings_path = "data/saltcon/settings.json"
        self.settings = dataIO.load_json(self.settings_path)
        self.valid_saltcons = ['1', '2', '3', '4', '5']

    @commands.command(name="saltcon", no_pm=True, pass_context=True)
    async def saltcon(self, ctx):
        """Reports the server saltcon level."""
        server = ctx.message.server
        self.load_settings(server)
        nick = self.settings[server.id]["authority"]
        await self.post_saltcon(str(self.settings[server.id]["saltcon"]), nick)

    @commands.command(name="saltcon+", no_pm=True, pass_context=True)
    async def saltconplus(self, ctx):
        """Elevates the server saltcon level."""
        server = ctx.message.server
        member = ctx.message.author
        self.load_settings(server)
        if self.settings[server.id]["saltcon"] == 1:
            await self.bot.say("We are already at SALTCON 1! Oh no!")
        else:
            self.settings[server.id]["saltcon"] -= 1

        self.settings[server.id]["authority"] = member.display_name
        self.save_settings(server)
        await self.post_saltcon(str(self.settings[server.id]["saltcon"]),
                               member.display_name)

    @commands.command(name="saltcon-", no_pm=True, pass_context=True)
    async def saltconminus(self, ctx):
        """Lowers the server saltcon level."""
        server = ctx.message.server
        member = ctx.message.author
        self.load_settings(server)
        if self.settings[server.id]["SALTCON"] == 5:
            await self.bot.say("We are already at saltcon 5! Relax!")
        else:
            self.settings[server.id]["SALTCON"] += 1

        self.settings[server.id]["authority"] = member.display_name
        self.save_settings(server)
        await self.post_saltcon(str(self.settings[server.id]["SALTCON"]),
                               member.display_name)

    @commands.command(name="setsaltcon", no_pm=True, pass_context=True)
    async def setsaltcon(self, ctx, level):
        """Manually set the server saltcon level in case of emergency."""
        server = ctx.message.server
        member = ctx.message.author
        self.load_settings(server)

        if level in self.valid_saltcons:
            self.settings[server.id]["SALTCON"] = int(level)
            self.settings[server.id]["Authority"] = member.display_name
            self.save_settings(server)
            await self.post_saltcon(str(self.settings[server.id]["saltcon"]),
                                   member.display_name)
        else:
            await self.bot.say("Not a valid SALTCON level. Haven't "
                               "you seen War Games?")

    async def post_saltcon(self, level, nick):

        icon_url = 'http://i.imgur.com/MfDcOEU.gif'

        if level == '5':
            color = 0x0080ff
            thumbnail_url = 'http://i.imgur.com/uTPeW7N.gif'
            author = "This server is at SALTCON LEVEL {}.".format(level)
            subtitle = ("No known NaCl related threats "
                        "exist at this time.")
            instructions = ("- Partipaction in online games is encouraged\n"
                            "- Remain vigilant of insider threats\n"
                            "- Report all suspicious activity")
        elif level == '4':
            color = 0x00ff00
            thumbnail_url = 'http://i.imgur.com/siIWL5V.gif'
            author = "This server is at SALTCON LEVEL {}.".format(level)
            subtitle = 'Trace amounts of sodium have been detected.'
            instructions = ("- Inhale deeply through your nose and "
                            "count to 5\n"
                            "- Take short breaks between games\n"
							"- avoid interactions with Arizeen\n"
                            "- Do not encourage trolls")
        elif level == '3':
            color = 0xffff00
            thumbnail_url = 'http://i.imgur.com/E71VSBE.gif'
            author = "This server is at SALTCON LEVEL {}.".format(level)
            subtitle = 'Sodium levels may exceed OSHA exposure limits.'
            instructions = ("- Use extreme caution when playing ranked games\n"
                            "- Log off non-essential communication channels\n"
                            "- Put on your big boy pants")
        elif level == '2':
            color = 0xff0000
            thumbnail_url = 'http://i.imgur.com/PxKhT7h.gif'
            author = "This server is at saltcon LEVEL {}.".format(level)
            subtitle = 'Sodium levels are approaching critical mass'
            instructions = ("- Avoid ranked game modes at all costs\n"
                            "- Mute all hostile voice channels\n"
                            "- Queue up some relaxing jazz music")
        elif level == '1':
            color = 0xffffff
            thumbnail_url = 'http://i.imgur.com/wzXSNWi.gif'
            author = "This server is at saltcon LEVEL {}.".format(level)
            subtitle = 'Total destruction is IMMINENT.'
            instructions = ("- Do not participate in any online games\n"
                            "- Log off all social media immediately\n"
                            "- Take shelter outdoors until the "
                            "all-clear is given")

        if level in self.valid_saltcons:
            embed = discord.Embed(title="\u2063", color=color)
            embed.set_author(name=author, icon_url=icon_url)
            embed.set_thumbnail(url=thumbnail_url)
            embed.add_field(name=subtitle, value=instructions, inline=False)
            embed.set_footer(text="Authority: {}".format(nick))
            await self.bot.say(embed=embed)
        else:
            await self.bot.say("Something wrent wrong.")

    def load_settings(self, server):
        self.settings = dataIO.load_json(self.settings_path)
        if server.id not in self.settings.keys():
            self.add_default_settings(server)

    def save_settings(self, server):
        if server.id not in self.settings.keys():
            self.add_default_settings(server)
        dataIO.save_json(self.settings_path, self.settings)

    def add_default_settings(self, server):
        self.settings[server.id] = {"saltcon": 5, "authority": "none"}
        dataIO.save_json(self.settings_path, self.settings)


def check_folders():
    folder = "data/saltcon"
    if not os.path.exists(folder):
        print("Creating {} folder...".format(folder))
        os.makedirs(folder)


def check_files():
    default = {}
    if not dataIO.is_valid_json("data/saltcon/settings.json"):
        print("Creating default saltcon settings.json...")
        dataIO.save_json("data/saltcon/settings.json", default)


def setup(bot):
    check_folders()
    check_files()
    n = saltcon(bot)
    bot.add_cog(n)