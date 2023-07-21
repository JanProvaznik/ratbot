import discord
import asyncio
from discord_bot import config
from discord_bot.message_handler import MessageHandler
from discord_bot.react_handler import ReactHandler

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        handler = MessageHandler(self, message)
        await handler.process()

    async def on_reaction_add(self, reaction, user):
        handler = ReactHandler(self, reaction, user)
        await handler.process()

client = MyClient()
client.run(config.BOT_TOKEN)