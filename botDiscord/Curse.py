from discord.ext import commands
import random

client = commands.Bot(command_prefix = ">", case_intensitive = True)

@client.event
async def on_ready():
    print("Entramos como {0.user}".format(client))

@client.command()
async def roi(ctx):
    await ctx.send(f'ola, {ctx.author}')

@client.command()
async def d(ctx, numero):
    variável = random.randint(1, int(numero))
    await ctx.send(f'{variável}')

@client.command()
async def c(ctx, numero):
    for i in range(1, int(numero)+1):
        curse = random.randint(1, 1001)
        if(curse==1):
            await ctx.send(f'[1] -O conjurador morreu: {curse}')
        elif(curse >= 2 and curse <= 50):
            await ctx.send(f'[2~50] -Causar 5% de dano no inimigo: {curse}')
        elif(curse >= 51 and curse <= 100):
            await ctx.send(f'[51~100] -Ganhar 5% de Souls: {curse}')
        elif (curse >= 101 and curse <= 130):
            await ctx.send(f'[101~130] -Causar 5% de dano: {curse}')
        elif (curse >= 131 and curse <= 150):
            await ctx.send(f'[131~150] -Cause 5% de dano no inimigo: {curse}')
        elif (curse >= 151 and curse <= 175):
            await ctx.send(f'[151~175] -Roda +3 curses: {curse}')
        elif (curse >= 176 and curse <= 200):
            await ctx.send(f'[176~200] -Inimigo mais próximo é puxado até você: {curse}')
        elif (curse >= 201 and curse <= 230):
            await ctx.send(f'[201~230] - Você é puxado pelo inimigo mais próximo: {curse}')
        elif (curse >= 231 and curse <= 250):
            await ctx.send(f'[231~250] -Causa cegueira por 1 turno: {curse}')
        elif (curse >= 251 and curse <= 275):
            await ctx.send(f'[251~275] -Desativar Efeito de condição por 1 turno: {curse}')
        elif (curse >= 276 and curse <= 300):
            await ctx.send(f'[276~300] - Inimigo não irá lhe atacar por 1 turno (em x1 o inimigo guarda 1 turno): {curse}')
        elif (curse >= 301 and curse <= 350):
            await ctx.send(f'[301~350] -Cause silencio no inimigo por 1 turno (não acumula): {curse}')
        elif (curse >= 351 and curse <= 400):
            await ctx.send(f'[351~400] -Ganhar 5% de souls: {curse}')
        elif (curse >= 401 and curse <= 450):
            await ctx.send(f'[401~450] -Causa Sangramento por 2 turnos, causando 5% de dano por turno: {curse}')
        elif (curse >= 451 and curse <= 500):
            await ctx.send(f'[451~500] -Causa 5% de dano: {curse}')
        elif (curse >= 501 and curse <= 550):
            await ctx.send(f'[501~550] -Use uma habilidade de raça aleatória do inimigo: {curse}')
        elif (curse >= 551 and curse <= 600):
            await ctx.send(f'[551~600] -Seu próximo ataque é 100% de acerto critico: {curse}')
        elif (curse >= 601 and curse <= 650):
            await ctx.send(f'[601~650] -Enraizar inimigo por 1 turno: {curse}')
        elif (curse >= 651 and curse <= 700):
            await ctx.send(f'[651~700] -Causa 150% de dano no próximo ataque: {curse}')
        elif (curse >= 701 and curse <= 725):
            await ctx.send(f'[701~725] -Inimigo sofre Exposto por 1 turno: {curse}')
        elif (curse >= 726 and curse <= 750):
            await ctx.send(f'[726~750] -Inimigo não Pode usar a raça por 1 turno: {curse}')
        elif (curse >= 751 and curse <= 775):
            await ctx.send(f'[751~775] -Impede o próximo contra-ataque inimigo: {curse}')
        elif (curse >= 776 and curse <= 800):
            await ctx.send(f'[776~800] -Impede o próximo de uma criação de souls: {curse}')
        elif (curse >= 801 and curse <= 850):
            await ctx.send(f'[801~850] -Inimigo fica desarmado por 1 turno: {curse}')
        elif (curse >= 851 and curse <= 875):
            await ctx.send(f'[851~875] -Você ganha a arma do inimigo por 1 turno: {curse}')
        elif (curse >= 876 and curse <= 900):
            await ctx.send(f'[876~900] -Todos perdem 20% de vida (aliado e inimigo): {curse}')
        elif (curse >= 901 and curse <= 910):
            await ctx.send(f'[901~910] -Todos os inimigos perdem 20% de vida (inimigos): {curse}')
        elif (curse >= 911 and curse <= 921):
            await ctx.send(f'[911~921] -Todos os aliados perdem 15% de vida (aliados): {curse}')
        elif (curse >= 922 and curse <= 930):
            await ctx.send(f'[922~930] -Todos irão me atacar (aliados irão tentar defender): {curse}')
        elif (curse >= 931 and curse <= 950):
            await ctx.send(f'[931~950] -Alguém vai ficar com 0% de Souls decidido no dado: {curse}')
        elif (curse >= 951 and curse <= 960):
            await ctx.send(f'[951~960] -Inimigo Fica imóvel por 1 turno: {curse}')
        elif (curse >= 961 and curse <= 970):
            await ctx.send(f'[961~970] -Eu recebo 5 curses: {curse}')
        elif (curse >= 971 and curse <= 980):
            await ctx.send(f'[971~980] -Todos perdem as reduções de dano, ninguém pode se defender até o final da luta: {curse}')
        elif (curse >= 981 and curse <= 999):
            await ctx.send(f'[981~999] -Todos ficam com 1% de vida e 1% de souls: {curse}')
        elif (curse == 1000):
            await ctx.send(f'[1000] -O inimigo irá morrer: {curse}')

client.run('discordTokenHere')