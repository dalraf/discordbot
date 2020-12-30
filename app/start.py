# bot.py
import os
from random import randrange

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='testar', help='Simula ação do jogo: Status Nível Dificuldade')
async def testar(ctx, status: int , nivel: int , dificuldade: int):
    print("Recebendo teste de Status=" + str(status) + ", Nível=" + str(nivel) + ", Dificuldade=" + str(dificuldade))
    pontos = randrange(20)
    saldo = ((status - pontos ) * nivel) - dificuldade
    print("Resultado=" + str(saldo))
    await ctx.send(str(saldo))

bot.run(TOKEN)
