
import os
import difflib
import sqlite3
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
from discord_webhook import DiscordWebhook


cid = 1186736174526627891
TOKEN = os.getenv("token")



editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)
import time
import random



@tasks.loop(seconds=7)
async def spammer():
  text_channel = client.get_channel(cid)

  if text_channel != None:
    text = " ** lupta tarfo ** "
    await text_channel.send(text)
    intervals = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    await asyncio.sleep(random.choice(intervals))

  spammer.start()
spammer.start()

@client.command()
async def stop(ctx):
    spammer.stop()

@client.command()
async def spam(ctx):
  spammer.start()

keep_alive()
client.run("token", bot=False)