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
    :warning: Varování pro:
    {0}
   
    Z dúvodu:
    {1} :warning: """.format(userName,message))
    
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
   channel = discord.utils.get(client.get_all_channels(), name='warn-logs')

   

    await client.ban(user)
    await client.send_message(channel, """
    :warning: Ban pro:
    {0}
   
    Z dúvodu:
    {1} :warning: """.format(userName,message))
    
    except discord.Forbidden:

        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('ban failed.')
        return		 



@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await client.say('Ban list is empty.')
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('unban failed.')
        return		      	 		 		  
  

client.run(os.getenv("BOT_TOKEN"))
#***Made by Nela!***
