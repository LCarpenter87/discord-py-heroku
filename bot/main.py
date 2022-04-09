import discord
import os
import psycopg2
from discord.ext import commands

DATABASE_URL = os.getenv('DATABASE_URL')
bot = commands.Bot(command_prefix="!")
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def redeem(ctx, code):
    author  = ctx.author
    valid_codes = ['alphabet', 'bubbles', 'cat']
    
    disallowed_users = ['HaroldSaxon', 'Macrologia']
    if ctx.author.name in disallowed_users:
        await ctx.reply(f'Sorry. {author} is not allowed to enter')
        return None
    
    if code in valid_codes:
        await ctx.reply(f"{ctx.author.name} You redeemed: {code}")
    else: 
        await ctx.send('Invalid, sorry')
    
if __name__ == "__main__":
    bot.run(TOKEN)
