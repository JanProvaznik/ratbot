import discord
from discord.ext import commands

class ReactHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return

        message = reaction.message
        if not message.author.bot:
            return

        emoji = reaction.emoji
        if str(emoji) == "👍":
            await message.channel.send(f"{user.mention} liked this message!")
        elif str(emoji) == "👎":
            await message.channel.send(f"{user.mention} disliked this message!")

def setup(bot):
    bot.add_cog(ReactHandler(bot))