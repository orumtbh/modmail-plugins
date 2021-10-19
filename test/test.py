import asyncio
import aiohttp
import discord
import math
import random
import time
from datetime import datetime
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

client = Bot (description="DESCRIPTION", command_prefix="PREFIX")

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
	print(discord.__version__)
	await client.change_presence(game=discord.Game(name="Just ping me!"))
	
@client.event
async def on_message(message):
	possible = ["<@!506158857098362890>", "<@506158857098362890>"]
	author = message.author
	server = message.server
	giverole = discord.utils.get(server.roles, id='506157422574829587')
	if message.content in possible:
		if 'Giveaway' in [y.name for y in message.author.roles]:
			await client.remove_roles(author, giverole)
			await client.send_message(message.channel, "{}, I've unsubscribed you from the giveaway pings.".format(author.mention))
		else:
			await client.add_roles(author, giverole)
			await client.send_message(message.channel, "{}, I've subscribed you to the giveaway pings.".format(author.mention))
	else:
		pass
		 

client.run('TOKEN')
