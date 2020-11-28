# bot.py
import os
from random import randrange

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='dados', help='Simular jogar dados.')
async def dados(ctx):
    await ctx.send(str(randrange(20)))

bot.run(TOKEN)