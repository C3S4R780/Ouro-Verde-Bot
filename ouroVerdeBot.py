# Imports
import nextcord
import os
from apiKeys import *
from nextcord.ext import commands

# Global variables
activity = nextcord.Activity(type=nextcord.ActivityType.listening, name="/tocar")
intents = nextcord.Intents.all()
client = commands.Bot(activity=activity, intents=intents)

initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)

# Start bot
client.run(BOTTOKEN)