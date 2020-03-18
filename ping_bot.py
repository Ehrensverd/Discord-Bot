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

    guild = discord.utils.find(lambda g: g.name == 'Reverends Sanctuary', client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    handler.select()
    member = discord.utils.find(lambda m: m.id == 166005373356998656, guild.members)
    handler.insert_user(member)
    handler.select()
    member_list = guild.members



    member_dict = {}
    for x in member_list:
        member_dict[x.id] = x



    print('\n\n ', member_dict[166005373356998656], '\n\n')


    for k, v in member_dict.items():
        print(k, '---->', v.name, '  :   ', v.id, '      ', v.discriminator )

    members = '\n'.join(member.name for member in guild.members)
    print(f'Guild Members:\n - {members}')



    print(f'{client.user} has connected to Discord!')


client.run(BOT_TOKEN)
