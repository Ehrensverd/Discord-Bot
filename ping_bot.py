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

bot = commands.Bot(command_prefix='!')
handler = db_handler

boterate = boterator.BotOperator()


# Bot runtime events:

@bot.event
async def on_ready():

    guild = discord.utils.find(lambda g: g.name == 'Reverends Sanctuary', bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    #Send members to boterator to ensure db is synced
    boterate.sync_members(guild.members)
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_member_join(member):
    """Add member when they join server. Check if they exist in db"""
    if boterate.has_member(member):
        boterate.update_member(member)
    else:
        boterate.insert_user(member)


@bot.event
async def on_member_update(old, updated):
    """ Is called when member changes status, activity, nickname roles

        db only has nickname stored so the other changes are ignored.
    """
    if old.nick != updated.nick:
        boterate.update_member(updated)


@bot.event
async def on_user_update(old, updated):
    """ Is called when user changes avatar,username or discriminator"""
    print('Updating user: ', old , ' to : ', updated)
    guild = discord.utils.find(lambda g: g.name == 'Reverends Sanctuary', bot.guilds)
    member = discord.utils.find(lambda m: m.id == updated.id, guild.members)
    if old.name != updated.name or old.discriminator != updated.discriminator:
        boterate.update_member(member)





#Commands:



@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


bot.run(BOT_TOKEN)

