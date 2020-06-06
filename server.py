import discord 
from discord.ext import commands
from discord.utils import get
import inspect
import datetime
import time
import os
import inspect

client = commands.Bot(command_prefix = "-")
client.remove_command("help")

tt = os.environ.get("TOKEN")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.dnd,activity=discord.Game("Снятие тупых модераторов."))
  while True:
    now = str(datetime.datetime.now())
    min = now.split(":")[1]
    hour = now.split(":")[0].split(" ")[1]
    second = now.split(":")[2].split(".")[0]
    if int(min) % 10 == 0:
      await client.get_channel(714136573079453799).send('<@&714138893036814397> скоро обновится!')
      if int(min) % 4 == 0:
        await client.get_channel(714136573079453799).send('<@&718816998540181604> скоро обновится!')
      time.sleep(60)
    if (int(hour) == 15 and int(min) == 53) or (int(hour) == 9 and int(min) == 53):
      await client.get_channel(714136573079453799).send('<@&714144632111366154> совсем скоро!')
      time.sleep(60)
    if min == '04':
      await client.get_channel(714136573079453799).send('<@&714174328488591490> сработали!')
      await client.get_channel(714136573079453799).send('<@&718816998540181604> скоро обновится!')
      time.sleep(60)
    if int(min) % 4 == 0 and int(min) % 10 != 0:
      await client.get_channel(714136573079453799).send('<@&718816998540181604> скоро обновится!')
      time.sleep(60)
      
client.run(tt)
