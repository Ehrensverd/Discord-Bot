from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import boterator
import time

class Looper:
    load_dotenv()
    BOT_TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD_ID = os.getenv('GUILD_ID')
    boterate = boterator.BotOperator()

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop()
    async def ping_event_ongoing(self):
        print('On going ping', time.time())
        self.boterate.add_new_ping_start()
        await self.bot.get_guild(int(self.GUILD_ID)).get_channel(689397500863578122).send('!PING')




"""

@ping_event_ongoing.after_loop
async def change_time():
    ping_event_ongoing.stop()


"""