# -*- coding: utf-8 -*-

import os
from random import randrange

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='testar', help='Simula ação do jogo')
async def testar(ctx, status: int , nivel: int , dificuldade: int):
    print("Recebendo teste de Status=" + str(status) + ", Nivel=" + str(nivel) + ", Dificuldade=" + str(dificuldade))
    pontos = randrange(20)
    saldo = ((status - pontos ) * nivel) - dificuldade
    print("Resultado=" + str(saldo))
    await ctx.send("O resutado da jogada é " + str(saldo))

@bot.command(name='rolar', help='Joga dados d20')
async def rolar(ctx):
    pontos = randrange(20)
    print("Resultado=" + str(pontos))
    await ctx.send("O resutado do dado é " + str(pontos))


bot.run(TOKEN)
