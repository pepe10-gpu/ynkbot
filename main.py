import discord
from discord.ext import commands
import discord.utils
import random
f = open("token.txt","r")
yag = ["made by yoink!", "bababooey", "Minecraft 1.8!", "at home!", "Minecraft 1.16!", "with cats!", "Among us!", "Terraria", "with python!", "with 24 lines of code!", ""]
token = f.read()
global role
role = str(input("what role? imput the NAME not id"))
bot = commands.Bot(command_prefix='ynk ')
@bot.command(pass_context=True)
async def verify(ctx):
    user = ctx.message.author 
    role #change the role here
    try:
        await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
        print("verified: " + str(user))
    except Exception as e:
        await ctx.send('Cannot verify. Error: ' + str(e))
        print('uh oh.' + str(e))
    await bot.change_presence(activity=discord.Game(name=yag[random.randint(0,(len(yag) - 1))]))
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=yag[random.randint(0,(len(yag) - 1))]))
print("test")
bot.run(token)
print("test")
#thats it no like youre done with this
