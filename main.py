import discord
from discord.ext import commands
import random

# دروستکردنی ڕێپێدانەکان (Intents) بۆ ئەوەی بۆتەکە بتوانێت نامەکان بخوێنێتەوە
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

# دیاریکردنی پاشگری فەرمانەکان (بۆ نموونە: help+)
bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'🔥 بۆتەکە بە سەرکەوتوویی ئۆنلاین بوو وەک: {bot.user.name}')
    print('🎮 هەموو فەرمانەکان و یارییەکان پێکەوە کۆکراونەتەوە و ئامادەن!')
    print('--------------------------------------------------')

# 📜 ١. لیستی گشتی فەرمانەکان (سەرەتایی + یارییەکان)
@bot.command()
async def helpme(ctx):
    help_text = (
        "📜 **لیستی گشتی فەرمانەکانی بۆتەکە:**\n\n"
        "ℹ️ **فەرمانە سەرەتاییەکان:**\n"
        "🔹 `+helpme` - نیشاندانی ئەم نامەیە\n"
        "🔹 `+spy` - تاقیکردنەوە و چاودێری سیستەمی بۆتەکە\n\n"
        "🎮 **بەشی یارییەکان:**\n"
        "🔹 `+fish` - 🎣 یاری ڕاوە ماسی (بزانە چی ڕاو دەکەیت!)\n"
        "🔹 `+rps [rock/paper/scissors]` - ✂️ یاری بەرد، مقەست، کاغەز لەگەڵ بۆتەکە\n"
        "🔹 `+roll` - 🎲 هاویشتنی زار (ژمارەیەک لە ١ تا ٦)\n"
        "🔹 `+coin` - 🪙 هاویشتنی دراو (شێر یان ڕێوی)"
    )
    await ctx.send(help_text)

# 🕵️‍♂️ ٢. فەرمانی سیستەمی Spy
@bot.command()
async def spy(ctx):
    await ctx.send("🕵️‍♂️ سیستەمی چاودێری چالاکە و بۆتەکە بە تەواوی کار دەکات!")

# 🎣 ٣. یاری ڕاوە ماسی (Fishing Game)
@bot.command()
async def fish(ctx):
    fish_list = [
        "🐟 ماسییەکی بچووکت ڕاوکرد!", 
        "🐠 ماسییەکی ڕەنگاوڕەنگی جوانت گرت!", 
        "🦈 واااو! نەهەنگێکی گەورەت ڕاوکرد!", 
        "🦀 قڕژاڵێکی توڕەت گرت!", 
        "👞 ئۆو نەخێر.. تەنها پێڵاوێکی کۆنت ڕاوکرد!"
    ]
    result = random.choice(fish_list)
    await ctx.send(f"🎣 {ctx.author.mention} قولاپی هاویشت و...\n**{result}**")

# ✂️ ٤. یاری بەرد، مقەست، کاغەز (Rock, Paper, Scissors)
@bot.command()
async def rps(ctx, choice: str = None):
    if not choice or choice.lower() not in ['rock', 'paper', 'scissors']:
        await ctx.send("❌ تکایە فەرمانەکە بەم شێوەیە بنووسە: `+rps rock` یان `paper` یان `scissors`")
        return
    
    bot_choice = random.choice(['rock', 'paper', 'scissors'])
    user_choice = choice.lower()
    
    await ctx.send(f"🤖 من **{bot_choice}**م هەڵبژارد!")
    
    if user_choice == bot_choice:
        await ctx.send("🤝 یەکسان بوون!")
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        await ctx.send(f"🎉 پیرۆزە {ctx.author.mention}! تۆ بردەتەوە! 😎")
    else:
        await ctx.send("😢 من بردمەوە! جارێکی تر تاقی بکەرەوە.")

# 🎲 ٥. یاری زار (Dice Roll)
@bot.command()
async def roll(ctx):
    dice_result = random.randint(1, 6)
    await ctx.send(f"🎲 {ctx.author.mention} زارەکەی هاویشت و ژمارە **{dice_result}**ی بۆ هات!")

# 🪙 ٦. یاری شێر یان ڕێوی (Coin Flip)
@bot.command()
async def coin(ctx):
    result = random.choice(["شێر (Heads)", "ڕێوی (Tails)"])
    await ctx.send(f"🪙 دراوەکە هاویشترا و هاتەوە سەر: **{result}**")

# جێگیرکردنی تۆکنە فەرمییەکەی خۆت بۆ بەستنەوەی بە دیسکۆردەوە
bot.run('MTUwOTUxNzA3MDk1Njc1NzEwMw.GPno35.PpOH1aD8nDa5Vu1Zo2tBlyTfZgEycDr3Y2DHoQ')
