import discord
from discord.ext import commands
from Scripts import custom_commands


IS_HEROKU = False
if IS_HEROKU:
    import os
    from boto.s3.connection import S3Connection
else:
    import env




# secret token NjQwNTc5NjExMjYwMDkyNDc1.Xb76tQ.JMNdIQezzEfkEm81Ap-8Q_Poo9k

client = commands.Bot(command_prefix="$")

custom_commands.set_commands(client)
if IS_HEROKU:
    s3 = S3Connection(os.environ['SECRET_TOKEN_KEY'])
    client.run(s3)
else:
    client.run(env.SECRET_TOKEN)

