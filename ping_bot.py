# bot.py
import db_handler
import boterator
import os
import random
from discord.ext import commands, tasks
from dotenv import load_dotenv
import looper

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

bot = commands.Bot(command_prefix='!')
handler = db_handler

boterate = boterator.BotOperator()
loop = looper.Looper(bot)

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
    loop.ping_event_ongoing.start()


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



@tasks.loop(seconds=24)
async def mainloop():
    print('\n\nStarting mainloop')
    #await bot.get_guild(int(GUILD_ID)).get_channel(689397500863578122).send('time is 22:00')
    #await bot.wait_until_ready()



    #print('inn main loop, changing interval')
    #loop.ping_event_ongoing.change_interval(seconds=boterate.get_time_interval())
    print('inn main loop, between change and start')
    loop.ping_event_ongoing.start()
    print('End of mainloop')





#Commands:


@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


bot.run(BOT_TOKEN)

"""


@bot.command()
async def pong(ctx):
    #get time and scored if player has not scored
    member = ctx.get_member
    await boterate.check_if_scored(member)
    
    @mainloop.before_loop
async def premain():
    boterate.first_ping_event()
    
    """