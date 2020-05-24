import discord 
from discord.ext import commands
from discord.utils import get
import inspect
import datetime
import time
import os

client = commands.Bot(command_prefix = "-")
client.remove_command("help")

tt = os.environ.get("TOKEN")

@client.event
async def on_ready():
  while True:
    now = str(datetime.datetime.now())
    min = now.split(":")[1]
    hour = now.split(":")[0].split(" ")[1]
    if int(min) % 10 == 0:
      await client.get_channel(714136573079453799).send('<@&714138893036814397>, àäñêàÿ øàõòà ñêîðî îáíîâèòñÿ!')
      time.sleep(60)
    if (int(hour) == 15 and int(min) == 53) or (int(hour) == 9 and int(min) == 53):
      await client.get_channel(714136573079453799).send('<@&714144632111366154>, ñîâñåì ñêîðî ñëóæåíèå!')
      time.sleep(60)
  
client.run(tt)
