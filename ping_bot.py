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

    member = discord.utils.find(lambda m: m.id == 166005373356998656, guild.members)

    handler.insert_user(member)
    handler.select()

    # Get Array of members
    member_list = guild.members

    #Put members in dictionary with their ID as key
    member_dict = {}
    for x in member_list:
        member_dict[x.id] = x

    #Send members to boterator to ensure db is synced
   # boterate.sync_members(member_dict)


    print(f'{client.user} has connected to Discord!')


client.run(BOT_TOKEN)





# code snippets
"""
find spesified member 
member = discord.utils.find(lambda m: m.id == 166005373356998656, guild.members)

"""