class Cybil:
    def __init__(self, bot):
        self.bot = bot

    async def listener(self, message):
        if message.author.id != self.bot.user.id:
            if 'blowjob' in message.content.lower() or 'hummer' in message.content.lower() or 'blowie' in message.content.lower():
                await self.bot.send_message(message.channel, 'Did someone mention a blowjob because, I mean lets talk prices.')


def setup(bot):
    n = Cybil(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)