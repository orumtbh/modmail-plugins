import asyncio
import aiohttp
import discord
import math
import random
import time
from datetime import datetime
from discord.ext import commands

    @bot.command(pass_context=True)
    @commands.has_role("Admin")
    async def unmute(ctx, user: discord.Member):
        role = discord.utils.find(lambda r: r.name == 'Yaksha', ctx.message.server.roles)
        if role in user.roles:
            await bot.say("{} is not muted".format(user))
        else:
            await bot.add_roles(user, role)
