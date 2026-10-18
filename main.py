import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="hola", description="El bot te saluda")
async def hola(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hola {interaction.user.mention}! Bot funcionando desde teléfono 📱")

@bot.tree.command(name="ping", description="Ver latencia")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong {round(bot.latency*1000)}ms")

bot.run(os.getenv("TOKEN"))
