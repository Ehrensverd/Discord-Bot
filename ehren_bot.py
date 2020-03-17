# bot.py
import db_handler
import os
import discord
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

client = discord.Client()
handler = db_handler





@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.id == GUILD_ID, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members_name = '\n'.join(member.name for member in guild.members)


    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    print(f'{client.user} has connected to Discord!')
    handler.test()

client.run(BOT_TOKEN)
