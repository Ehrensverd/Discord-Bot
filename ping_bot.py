# bot.py
import db_handler
import boterator
import os
import discord
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

client = discord.Client()
handler = db_handler

boterate = boterator.BotOperator()



@client.event
async def on_ready():

    guild = discord.utils.find(lambda g: g.name == 'Reverends Sanctuary', client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    #Send members to boterator to ensure db is synced
    boterate.sync_members(guild.members)


    print(f'{client.user} has connected to Discord!')


client.run(BOT_TOKEN)

