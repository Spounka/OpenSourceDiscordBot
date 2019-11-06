import discord
from discord.ext import commands


def set_commands(bot : commands.Bot):
    @bot.command()
    async def greet(ctx):
        await ctx.send("Yo")

    @bot.command()
    async def setNickname(ctx, nickname=None):
        if (await bot.is_owner(ctx.author)):
            await ctx.send("Owner! can't change nickname")
            return
        if nickname is None:
            ctx.author.edit(nick="")
        else:
            ctx.author.edit(nick=nickname)

    @bot.command()
    async def changeUserNick(ctx, user, nickname=None):
        member = ctx.guild.get_member_named(user)
        if member is None:
            await ctx.send("Member Not Found!")
        elif nickname is not None:
            await member.edit(nick=nickname)
        
    @bot.command()
    async def sendImage(ctx):
        # img = discord.File("image.jpg", "meme")
        await ctx.send(file=discord.File(fp="pictures/empale.jpg"))
    
    @bot.command()
    async def listUsers(ctx):
        for guild in bot.guilds:
            for member in guild.members:
                if not (await bot.is_owner(ctx.author)):
                    await ctx.send(member.name)