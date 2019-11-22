import discord
from discord.ext import commands



""" *****   Checks   ***** """

async def is_Admin(self, ctx):
    if (await self.bot.is_owner(ctx.author)):
        return True
    for role in ctx.guild.roles:
        if role.name.lower() == "moderator":
            return ctx.author.top_role >= role

async def get_default_channel(bot):
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name.lower() == "discussion" and channel.category.name.lower() == "general":
                return channel

def get_departments(member):
    roles = member.guild.roles
    roles = roles[1:7]
    return roles


class ChannelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="lists the all the users in the server")
    async def listUsers(self, ctx):
        for member in ctx.guild.members:
            await ctx.send(member.name)

    @commands.command(name="clean", help="cleans the channel messages")
    async def clean_channel(self, ctx):
        if not await is_Admin(self, ctx):
            await ctx.send("You Don't have the permission to clean the channel!")
            return
        messages = []
        async for message in ctx.channel.history(limit=1000):
            messages.append(message)
        async with ctx.channel.typing():
            while True:
                if len(messages) > 100:
                    await ctx.channel.delete_messages(messages[:100])
                else:
                    await ctx.channel.delete_messages(messages[:len(messages)])
                    break

class Editing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(help="Sets your desired departments, you can only have two and cannot change them")
    async def department(self, ctx, *, department1):
        if len(ctx.author.roles) > 3:
            await ctx.send("You cannot choose any more departments, already at the limit")

        else:
            departments = department1.split(", ")
            
            if(len(departments) > 2):
                await ctx.send("Can enter only two departments !")
            else:
                dep1, dep2 = False, False
                for role in get_departments(ctx.author):
                    if role.name.lower() == departments[0].lower():
                        await ctx.author.add_roles(role)
                        await ctx.send("Department {0} added Successfully".format(departments[0]))
                        dep1 = True

                    if len(departments) > 1 and departments[1].lower() == role.name.lower():
                        await ctx.author.add_roles(role)
                        await ctx.send("Department {0} added Successfully".format(departments[1]))
                        dep2 = True
                    if dep1 and dep2:
                        break
                else:
                    if not dep1:
                        await ctx.send("Department {0} Not Found".format(departments[0]))
                        await ctx.send("Available department are:\n" + '\n'.join([dep.name for dep in get_departments(ctx.author)]))
                    if not dep2:
                        await ctx.send("Department {0} Not Found".format(departments[1]))
                        await ctx.send("Available department are:\n" + '\n'.join([dep.name for dep in get_departments(ctx.author)]))

                
    @commands.command(help="Same as department")
    async def departement(self, ctx, *, department1):
        if len(ctx.author.roles) > 3:
            await ctx.send("You cannot choose any more departments, already at the limit")

        else:
            departments = department1.split(", ")
            
            if(len(departments) > 2):
                await ctx.send("Can enter only two departments !")
            else:
                dep1, dep2 = False, False
                for role in get_departments(ctx.author):
                    if role.name.lower() == departments[0].lower():
                        await ctx.author.add_roles(role)
                        await ctx.send("Department {0} added Successfully".format(departments[0]))
                        dep1 = True

                    if len(departments) > 1 and departments[1].lower() == role.name.lower():
                        await ctx.author.add_roles(role)
                        await ctx.send("Department {0} added Successfully".format(departments[1]))
                        dep2 = True
                    if dep1 and dep2:
                        break
                else:
                    if not dep1:
                        await ctx.send("Department {0} Not Found".format(departments[0]))
                        await ctx.send("Available department are:\n" + '\n'.join([dep.name for dep in get_departments(ctx.author)]))
                    if not dep2:
                        await ctx.send("Department {0} Not Found".format(departments[1]))
                        await ctx.send("Available department are:\n" + '\n'.join([dep.name for dep in get_departments(ctx.author)]))
                

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


    @commands.command(hidden=True)
    async def send_announcement(self, ctx, *, msg):
        if not await is_Admin(self, ctx):
            return
        for guild in self.bot.guilds:
            for category in guild.categories:
                for channel in category.channels:
                    if category.name.lower() == "general" and channel.name.lower() == "announcements":
                        await channel.send("@everyone " + str(msg))
                        await ctx.message.delete()


        
    @commands.command(help="sends an image", hidden=True)
    async def sendImage(self, ctx):
        pass




def set_commands(bot : commands.Bot):
    @bot.event
    async def on_member_join(member):
        member_role = member.guild.get_role(641779701915975710)
        await member.add_roles(member_role)
        channel = await get_default_channel(bot)
        roles = get_departments(member)
        await channel.send("Hello {0}, welcome to Open Source C.C\nUse $help to see commands\nType: $department {1} to join a department"
                           .format(member.mention, ', '.join([role.name for role in roles])))

    bot.add_cog(ChannelCommands(bot))
    bot.add_cog(Editing(bot))
    bot.add_cog(Communication(bot))

    


    

    
    