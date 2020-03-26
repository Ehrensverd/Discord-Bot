from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import boterator

from datetime import datetime, timedelta
from random import randint
import time


def make_random_time():
    # datetime.now().replace(hour=randint(7, 22), minute=randint(0, 59), second=randint(0, 59)) + timedelta(days=1)
    timestamp = datetime.now().astimezone() + timedelta(seconds=randint(6, 30))
    print('Random time stamp made:', timestamp)
    return timestamp


class Looper:
    load_dotenv()
    BOT_TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD_ID = os.getenv('GUILD_ID')
    boterate = boterator.BotOperator()
    sec_elapsed = time.time()

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=5)
    async def ping_event_handler(self):
        """Loop that checks whether its time to activate next ping       """

        nextping = self.boterate.get_ping_timestamp()
        if nextping is None:
            self.boterate.set_next_ping_timestamp(datetime.now())
            self.boterate.set_next_ping_timestamp(make_random_time())
            await self.bot.get_guild(int(self.GUILD_ID)).get_channel(689397500863578122).send('ping!')
            return

        nextping = nextping[0]
        print(datetime.now().astimezone())
        print(nextping)
        if nextping < datetime.now().astimezone():
            self.boterate.set_next_ping_timestamp(make_random_time())
            await self.bot.get_guild(int(self.GUILD_ID)).get_channel(689397500863578122).send('ping!')
        return
