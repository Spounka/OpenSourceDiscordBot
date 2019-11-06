import discord
from discord.ext import commands
from Scripts import custom_commands
import env



for i in range(10):
    print(i)


# secret token NjQwNTc5NjExMjYwMDkyNDc1.Xb76tQ.JMNdIQezzEfkEm81Ap-8Q_Poo9k

client = commands.Bot(command_prefix="$")

custom_commands.set_commands(client)
client.run(env.SECRET_TOKEN)

