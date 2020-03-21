# bot.py

import boterator
import os
from datetime import datetime, timedelta
from discord.ext import commands, tasks
from dotenv import load_dotenv
import looper


load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')
bot = commands.Bot(command_prefix='!')
boterate = boterator.BotOperator()
loop = looper.Looper(bot)

def main():
    bot.run(BOT_TOKEN)


# Bot runtime events:
@bot.event
async def on_ready():
    guild = bot.get_guild(int(GUILD_ID))
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    #Send members to boterator to ensure db is synced
    boterate.sync_members(guild.members)
    print(f'{bot.user} has connected to Discord!')
    #Start ping loop that handles ping game
    loop.ping_event_handler.start()


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
    member = bot.get_guild(int(GUILD_ID)).get_member(updated.id)
    if old.name != updated.name or old.discriminator != updated.discriminator:
        boterate.update_member(member)


#Commands:
@bot.command()
async def pong(ctx):
    """ Chat command used to score after 'ping!' is issued by bot. the faster the more points"""

    time_since_pong = datetime.now() - boterate.get_ongoing_ping_timestamp()
    print(time_since_pong)

    if not boterate.has_scored(ctx.author.id):
        points = boterate.update_member_score(ctx.author.id, time_since_pong)
        await bot.get_guild(int(GUILD_ID)).get_channel(689397500863578122).send('Scored points: ', points, 'You ponged withing ',time_since_pong, 'seconds.')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


if __name__ == "__main__":
    main()


