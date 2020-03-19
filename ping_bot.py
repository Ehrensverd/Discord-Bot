# bot.py
import db_handler
import boterator
import os
import discord
from discord.ext import commands
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

@client.event
async def on_member_join(member):
    """Add member when they join server. Check if they exist in db"""
    if boterate.has_member(member):
        boterate.insert_user(member)
    else:
        boterate.update_member(member)

@client.event
async def on_member_update(old, updated):
    """ Is called when member changes status, activity, nickname roles

        db only has nickname stored so the other changes are ignored.
    """
    if old.nick != updated.nick:
        boterate.update_member(updated)

@client.event
async def on_user_update(old, updated):
    """ Is called when user changes avatar,username or discriminator"""
    if old.name != updated.name or old.discriminator != updated.discriminator:
        boterate.update_member(updated)


    
client.run(BOT_TOKEN)

