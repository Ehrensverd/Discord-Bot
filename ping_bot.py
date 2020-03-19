# bot.py
import db_handler
import boterator
import os
import random
from discord.ext import commands, tasks
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
    guild = bot.get_guild(int(GUILD_ID))
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    #Send members to boterator to ensure db is synced
    boterate.sync_members(guild.members)
    print(f'{bot.user} has connected to Discord!')
    mainloop.start()


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




#Ping event



@tasks.loop(seconds=12)
async def mainloop():
    print('Starting mainloop')
    await bot.get_guild(int(GUILD_ID)).get_channel(689397500863578122).send('time is 22:00')
    await ping_event_ongoing.start()


#make before_loop av main
@mainloop.before_loop
async def premain():
    await boterate.first_ping_event()

@tasks.loop(seconds=boterate.get_time_interval(), count=2)
async def ping_event_ongoing():
    await bot.get_guild(int(GUILD_ID)).get_channel(689397500863578122).send('Ping loop started')


@ping_event_ongoing.after_loop
async def ping_start():
    """
    Ping!
    Start of ping event.
    calculates next ping
    which will end this ping event and start the next one
    Writes next ping to db
    id  | start    |   end
    1   |   12:24  |   15:23   interval is 24 hous plus 2h 59m - pingers next loop time.
    2   | 15:23    |    21:14

    Makes this ping active (True) - previous False



    next ping event.
    new pings score new event in db
    """

    await bot.get_guild(int(GUILD_ID)).get_channel(689397500863578122).send('!PING')
    next_day_ping = random.randrange(7, 22)
    boterate.add_new_ping_start(next_day_ping)


#Commands:



@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


bot.run(BOT_TOKEN)

