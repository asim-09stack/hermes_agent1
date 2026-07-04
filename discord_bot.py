import os
import discord
import asyncio
from agent import run_agent
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        user_input = message.content.replace("!ask", "").strip()
        await message.channel.send("🤔 Thinking...")

        try:
            reply = await asyncio.to_thread(run_agent, user_input)
            await message.channel.send(reply)
        except Exception as e:
            await message.channel.send("⚠️ Something went wrong.")
            print("Agent error:", e)

client.run(TOKEN)