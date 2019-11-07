import discord
from discord.ext import commands

class ChannelCommands(commands.Cog):
    def __init__(self, bot):
        super(ChannelCommands, self).__init__()
        self.bot = bot

    @commands.command(help="lists the all the users in the server")
    async def listUsers(self, ctx):
        for member in ctx.guild.members:
            await ctx.send(member.name)

    @commands.command(name="clean", help="cleans the channel messages")
    async def clean_channel(self, ctx):
        messages = []
        async for message in ctx.channel.history(limit=1000):
            messages.append(message)
        async with ctx.channel.typing():
            while True:
                if len(messages) > 100:
                    await ctx.channel.delete_messages(messages[:99])
                else:
                    await ctx.channel.delete_messages(messages[:len(messages)])
                    break

class Editing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="changes your nickname")
    async def setNickname(self, ctx, nickname=None):
        if (await self.bot.is_owner(ctx.author)):
            await ctx.send("Owner! can't change nickname")
            return
        if nickname is None:
            ctx.author.edit(nick="")
        else:
            ctx.author.edit(nick=nickname)

    @commands.command(help="changes the given user's nickname")
    async def changeUserNick(self, ctx, user, nickname=None):
        member = ctx.guild.get_member_named(user)
        if member is None:
            await ctx.send("Member Not Found!")
        elif await self.bot.is_owner(member):
            await ctx.send("Cant Edit Owner nickname")
            return
        else:
            await member.edit(nick=nickname)
            
class Communication(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if (await self.bot.is_owner(message.author)):
            if message.content.startswith(".send_announcement"):
                for guild in self.bot.guilds:
                    for category in guild.categories:
                        for channel in category.channels:
                            if category.name.lower() == "general" and channel.name.lower() == "announcements":
                                await channel.send("@everyone, an announcement")
                                await message.delete()

    @commands.command(help="greets the caller")
    async def greet(self, ctx):
        await ctx.send("Yo")

        
    @commands.command(help="sends an image")
    async def sendImage(self, ctx):
        await ctx.send(file=discord.File(fp="pictures/empale.jpg"))





def set_commands(bot : commands.Bot):
    bot.add_cog(ChannelCommands(bot))
    bot.add_cog(Editing(bot))
    bot.add_cog(Communication(bot))

    


    

    
    