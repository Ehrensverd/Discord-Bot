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
    sec_elapsed = time.time()

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop()
    async def ping_event_ongoing(self):
        # await self.bot.get_guild(int(self.GUILD_ID)).get_channel(689397500863578122).send('!PING')
        print('\nPING!\nPing Loop starting, last loop lasted:  ',  round((time.time() - self.sec_elapsed), 2))

        print('inserting this new ping event and finding start of next')
        self.boterate.add_new_ping_start()

        seconds = self.boterate.get_time_interval()
        print('Next interval is: ', seconds)
        print('Changing interval of next loop\n')
        self.ping_event_ongoing.change_interval(seconds=seconds)
        self.sec_elapsed = time.time()




"""

@ping_event_ongoing.after_loop
async def change_time():
    ping_event_ongoing.stop()


"""