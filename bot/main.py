import discord
import os
import psycopg2
from discord.ext import commands

DATABASE_URL = os.getenv('DATABASE_URL')
bot = commands.Bot(command_prefix="!")
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor() 
conn.autocommit = True 

TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

def validate_code(code, author):
    ## for now just checking that the code is still un-redeemed 
    ## to do is add the concept of many users being able to redeem a code one time. 
    
    cursor.execute(f"SELECT code from master_codes left outer join redemptions r using (code) where r.code IS NULL and code = '{code}'")
    rows = cursor.fetchall() 
    return len(rows) > 0
 
async def create_redemption(code, author):
    cursor.execute("INSERT INTO redemptions values (code, author) ")
    cursor.commit() 
    return 'Success'
    
@bot.command()
async def redeem(ctx, code):
    author  = ctx.author
    
    disallowed_users = ['HaroldSaxon', 'Macrologia']
    if ctx.author.name in disallowed_users:
        await ctx.reply(f'Sorry. {author} is not allowed to enter')
        return None
    
    if validate_code(code, author):
        create_redemption(code, author)
        
        if create_redemption(code, author) == 'Success': 
            await ctx.reply('Cool. Redeemed. #2')
        else:
            await ctx.reply('wut')
    else:
        await ctx.reply("Sorry, I couldn't redeem that")
        
    
if __name__ == "__main__":
    bot.run(TOKEN)
