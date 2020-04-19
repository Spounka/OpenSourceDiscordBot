import discord
from discord.ext import commands
from Scripts import custom_commands
import os

isHEROKU = True

client = commands.Bot(command_prefix="$")
custom_commands.set_commands(client)
client.run(os.environ['SECRET_TOKEN'])
