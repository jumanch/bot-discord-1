import discord
import datetime
import random
import math
import copy
from discord.ext import commands

bot = commands.Bot(command_prefix='·', description="El guardian de OPIPARO PEPINO.")

# Comando sueltos

@bot.command()
async def boss(ctx):
    await ctx.send("Ese nombre me suena e.e")

@bot.command()
async def lirin(ctx):
    await ctx.send("Lirin carry")


@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def motherfuker(ctx):
    await ctx.send("SOY UN HIJO DE PUTA QUE NO SE SUMAR")

# Operaciones aritmeticas 

@bot.command()
async def suma(ctx, n1: int,n2: int):
    solucion = n1 + n2
    if solucion == 0:
        await ctx.send("Tu no puedes sumar mas alpacas a la ruta de la leña si no tienes furgoneta.")
    else:
        await ctx.send("Entendido, la suma de {} mas {} da {}".format(n1,n2,solucion))

@bot.command()
async def resta(ctx, n1: int,n2: int):
    solucion = n1 - n2
    if solucion == 0:
        await ctx.send("Si tu tienes {} galletas y las repartes entre {} amigos, te sigues quedando con {} galletas.".format(n1,n2,n1))
    else:
        await ctx.send("Entendido, la resta de {} menos {} da {}".format(n1,n2,solucion))

@bot.command()
async def multiplica(ctx, n1: int,n2: int):
    solucion = n1 * n2
    await ctx.send("Entendido, la multiplicación de {} por {} da {}".format(n1,n2,solucion))

@bot.command()
async def eleva(ctx, n1: int,n2: int):
    solucion = n1 ** n2
    await ctx.send("Entendido, {} elevado a {} da {}".format(n1,n2,solucion))

@bot.command()
async def divide(ctx, n1: int,n2: int):
    solucion = n1 / n2
    try:
        if solucion == 0:
            await ctx.send("Si tu tienes {} galletas y las repartes entre {} amigos, te sigues quedando con {} galletas.".format(n1,n2,n1))
        else:
            await ctx.send("Entendido, la division de {} entre {} da {}".format(n1,n2,solucion))
    except:
        await ctx.send("No me hagas perder el tiempo.")

##### Mini- Juegos

@bot.command()


async def probabilidad(ctx,pregunta):
    
    probabilidad= int(random.randint(0, 100))
    if probabilidad > 9:
        probabilidad2 = copy.copy(probabilidad)
        probabilidad2 = float(probabilidad2/2)
        probabilidad2= math.ceil(probabilidad2)
        pass
    else:
        probabilidad2 = copy.copy(probabilidad)
        probabilidad2 = float(probabilidad2/2)
        probabilidad2= math.ceil(probabilidad2)
    separador = "x"
    respuesta= ""


    if probabilidad >= 90:
        respuesta=" - ¡Enhorabuena!"
    elif probabilidad in range(60,90):
        respuesta=" - Ni tan mal."
    elif probabilidad in range(40,60):
        respuesta=" - UUUUUUuufff."
    elif probabilidad in range(20,40):
        respuesta=" -Lo siento."
    else:
        respuesta="- F."

    embed = discord.Embed(title=f"PROBABILIDADES",description="""Hay un {}% de probabilidades de {}.

                 0%                     50%                       100%
                 A+++++++++++++++++++++++A+++++++++++++++++++++++A
                 A{}|
                 A+++++++++++++++++++++++A+++++++++++++++++++++++A
                 
                 Guardian{}""".format(probabilidad,pregunta,separador*probabilidad2,respuesta),color=discord.Color.blue())

    await ctx.send(embed=embed)
###################### Info del servidor
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="El mejor servidor jamás creado bla bla bla la culpa de Lirin siempre pero ojo, no abuses del meme o te banearé.",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name="Servidor creado en", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Región", value=f"{ctx.guild.region}")
    embed.add_field(name="ID Servidor", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Icon-round-Question_mark.svg/1024px-Icon-round-Question_mark.svg.png")
    
    await ctx.send(embed=embed)






# Evento
@bot.event
async def on_ready():
    game = discord.Game("Jugando a ser yo.. digo Dios")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Ya estoy online!')

bot.run("NTczODE4OTIwNTQ1NTUwMzM4.XMwZNw.9oZMRBa5cT37ZUqax5k5ZBJiAnw")