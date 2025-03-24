import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1325617668379770912
TARGET_USER_ID = 167480479040143360

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

    if message.channel.id == CHANNEL_ID:
        try:
            recipient = await bot.fetch_user(TARGET_USER_ID)
            await recipient.send(
                f"🔔 New message from **{message.author}** in {message.channel.mention}:\n{message.content}"
            )
        except Exception as e:
            print("❌ Failed to DM:", e)

    await bot.process_commands(message)

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(TOKEN)
