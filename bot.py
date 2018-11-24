import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = '/')



@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Prefix: /, Dev Nela"))
    print("The bot is online and connected with Discord!")


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)

async def warn(ctx, userName: discord.User, *, message:str):

    channel = discord.utils.get(client.get_all_channels(), name='warn-logs')
    await client.send_message(userName, "Byl jsi varován za: **{}**".format(message))
    await client.send_message(channel, """
    :warning: Varování pro:""" +
    userName + """
    Z dúvodu:
    {1} :warning: """.format(userName,message))
    


client.run(os.getenv("BOT_TOKEN"))
#***Made by Nela!***
