import discord

class TestClass(discord.Client):

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(".help"):
            await message.channel.send("Help menu, no commands availble at the moment")

client = TestClass()
client.run("NjQwNTc5NjExMjYwMDkyNDc1.Xb76tQ.JMNdIQezzEfkEm81Ap-8Q_Poo9k")


# secret token NjQwNTc5NjExMjYwMDkyNDc1.Xb76tQ.JMNdIQezzEfkEm81Ap-8Q_Poo9k
