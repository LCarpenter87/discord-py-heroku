import discord
import os
from datetime import date
from discord.ext import commands


bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def redeem(ctx, code):
    await ctx.send(f"You redeemed: {code}")
    
if __name__ == "__main__":
    bot.run(TOKEN)
