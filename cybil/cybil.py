class Cybilshit:
    def __init__(self, bot):
        self.bot = bot
        self.cybilshit = ["You mean nothing to me without wings in your hands {}! ~{}","Fuck you, {}. ~{}", "Fucking fuck off, {}. ~{}","Fuck off, {}. ~{}","Fuck this, {}. ~{}", "Fuck that, {}. ~{}","Eat a dick, {}. ~{}"]

    async def listener(self, message):
        if message.author.id != self.bot.user.id:
            if 'cybil' in message.content.lower():
                cybilfuck = randchoice(self.cybilshit)
                data = discord.Embed(colour=user.color)
                data.add_field(name="Message from Cybil:",value="{}".format(cybilfuck))                     
                await self.bot.send_message(message.channel, 'Did someone mention a blowjob because, I mean lets talk prices.')


def setup(bot):
    n = Cybilshit(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)
