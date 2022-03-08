import os
import discord
import time
import datetime
import requests
from keep_alive import keep_alive
from discord.ext import commands
from PIL import Image,ImageFont,ImageDraw

TOKEN  = os.environ['TOKEN']
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='q', description="Frenzy", intents=intents)

# Presence
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.watching, name =f"Frenzy TM"))
  print(f'Loggin Dis Bot {bot.user}')

# Ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping! {round(bot.latency * 1000)}ms")

# Banner
@bot.command()
async def banner(ctx):

    while True:
        vc = 0
        guild = bot.get_guild(835116243626491955)
        for member in ctx.guild.members:
            voice_state = member.voice
            if voice_state is None:
                continue
            else:
                vc += 1
        img = Image.open("image.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Font.ttf", 30)
        draw.text((233, 120), str(vc), (0,255,0), font=font)
        draw.text((332, 180), str(len(guild.members)), (0,255,0), font=font)
        img.save(f"{vc}.png")
        await ctx.send(file = discord.File(f"{vc}.png"),delete_after=0)
        os.remove(f"{vc}.png")
        time.sleep(10)
keep_alive() 
bot.run(TOKEN)
