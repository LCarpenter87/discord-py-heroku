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
    author  = ctx.author.name 
    valid_codes = ['alphabet', 'bubbles', 'cat']
    
    if author == 'HaroldSaxon':
        await ctx.send('Sorry. Lukas is not allowed to enter') 
   
    if author == 'Macrologia':
        await ctx.send('Sorry. Macrologia is not allowed to enter')     
    
    if code in valid_codes:
        await ctx.send(f"{ctx.author.name} You redeemed: {code}")
    else: 
        await ctx.send('Fuck off that aint a code')
    
if __name__ == "__main__":
    bot.run(TOKEN)
