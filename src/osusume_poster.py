import discord
from discord.ext import tasks, commands
import random

class OsusumePoster(commands.Cog):
    def __init__(self, bot: commands.Bot):
        print("init")
        self.bot = bot
        self.printer.start()
        self.index = 0
        self.in_channel_ids = []
        self.out_channel_id = 0
    
    def cog_unload(self):
        print("cog_unload")
        self.printer.cancel()

    @commands.command()
    async def link(self, ctx, set_type):
        print("link")
        # text channelしか登録できない
        if type(ctx.channel) is not discord.channel.TextChannel or ctx.channel.id in self.in_channel_ids:
            return

        if set_type == "in":
            self.in_channel_ids.append(ctx.channel.id)
        elif set_type == "out":
            self.out_channel_id = ctx.channel.id

    @commands.command()
    async def unlink(self, ctx, set_type):
        print("unlink")
        if set_type == "in" and ctx.channel.id in self.in_channel_ids:
            self.in_channel_ids.remove(ctx.channel.id)
        elif set_type == "out":
            self.out_channel_id = 0
    
    async def print_message(self):
        print("print_message")
        out_channel = self.bot.get_channel(self.out_channel_id)
        
        if out_channel == None:
            return
        message="**本日のおすすめ**\n"
        embed = discord.Embed(title="本日のおすすめ",color=0xff0000)

        for in_channel_id in self.in_channel_ids:
            in_channel = self.bot.get_channel(in_channel_id)
            messages = [message async for message in in_channel.history(limit=None)]
            if len(messages) == 0:
                continue
            choiced_message = None
            while_count = 0
            while choiced_message == None or not choiced_message.content.startswith("https://"):
                choiced_message = random.choice(messages)
                while_count += 1
                if while_count > 1000:
                    await out_channel.send("Invalid messages")
                    return

            message += "【" + in_channel.name + "】\n"
            message += choiced_message.content + "\n\n"
            embed.add_field(name=in_channel.name, value=choiced_message.content)

        await out_channel.send(message.rstrip())

    @commands.command()
    async def do_put(self, ctx):
        print("do_put")
        await self.print_message()

    @tasks.loop(hours=24)
    async def printer(self):
        print("printer")
        await self.print_message()

async def setup(bot):
    print("setup")
    await bot.add_cog(OsusumePoster(bot))