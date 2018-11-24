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
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    channel = discord.utils.get(client.get_all_channels(), name='warn-logs')
    await client.send_message(userName, "Byl jsi varován za: **{}**".format(message))
    await client.say("""
    :warning: Varování pro:
    __**{0}**__
    **Z dúvodu:
    {1}** """.format(userName,message))
    await client.send_message(channel, embed=discord.Embed(color=color))



client.run(os.getenv("BOT_TOKEN"))
