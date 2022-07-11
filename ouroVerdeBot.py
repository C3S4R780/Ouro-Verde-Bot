# Imports
import discord
import urllib.request
from apiKeys import *
from discord.ext import commands
from discord import FFmpegPCMAudio

# Global variables
activity = discord.Activity(type=discord.ActivityType.listening, name="!ov")
client = commands.Bot(command_prefix="!ov ", activity=activity)
RADIO_URL = "https://servidor18.brlogic.com:7484/live"

# Commands
# Command to call the bot into voice chat and play the radio's audio
@client.command(pass_context=True)
async def tocar(ctx):

    # If the command requester is currently on a voice channel...
    if (ctx.author.voice):

        # Checks if the radio is currently available before playing it
        requestStatus = urllib.request.urlopen(RADIO_URL).getcode()
        if (requestStatus == 200):
            source = FFmpegPCMAudio(RADIO_URL)
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            player = voice.play(source)
        else:
            await ctx.send("Parece que a radio está fora do ar no momento")
    else:
        await ctx.send("Você precisar estar em um canal de voz para usar este comando.")

# Command to remove the bot from the current voice channel
@client.command(pass_context=True)
async def sair(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Ainda não estou em nenhum canal de voz.")

# Start bot
client.run(BOTTOKEN)