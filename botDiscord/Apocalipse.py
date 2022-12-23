from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix = ">", case_intensitive = True)

@client.event
async def on_ready():
    print("Entramos como {0.user}".format(client))

@client.command()
async def b(ctx, base):
    base = int(base)
    tempo_final = random.randint(base-30, base)
    print(tempo_final)
    time.sleep(tempo_final)
    await ctx.send(f'O tempo final estimado é de: {tempo_final}')

client.run('ODcwMzI1NDA2NzM2MTk5NzMw.YQLHsg.tn5_4yc8nrwsl8SMz_wQmC718uM')