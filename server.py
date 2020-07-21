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

@client.command() 
async def ev(message,*command):
  if message.author.id == 529044574660853761:
    command = " ".join(command)
    res = eval(command)
    if inspect.isawaitable(res): 
      await message.channel.send('```py\n' + str(await res) + '```')
    else:
      await message.channel.send('```py\n' + str(res) + '```')
      
@client.command()
async def check(message, id=None):
  if id is None:
    id = message.author.id
  else:
    id = id.replace("!", "").replace("@","").replace("<","").replace(">","")
  a = await client.fetch_user(int(id))
  await message.channel.send(f'```css\nДата создания аккаунта {a}: {a.created_at}```')
  
client.run(tt)
