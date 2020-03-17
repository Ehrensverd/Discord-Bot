# bot.py
import DatabaseHandler
import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
handler = DatabaseHandler





@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    handler.test()

client.run(token)
