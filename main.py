import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.load_extension('osusume_poster')

# ホットリロード用
@bot.command()
async def reload(ctx: commands.Context):
    if ctx.message.author.id == 272646759229161473:
        await bot.reload_extension('osusume_poster')

bot.run("NDE4NDEwMTU4Mjg1MjU4NzYy.GqSSSv.KNuz2iSaKblAbJB33fCOzoM1iO81-01JE83SMw")
