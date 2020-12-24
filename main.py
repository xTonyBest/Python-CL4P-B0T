import discord
import os

greetings = ["hello", "ciao", "good morning", "buongiorno", "ciaone", "salve"]

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  for greeting in greetings:
    if message.content.toLowerCase.startswith(greeting):
      await message.channel.send("Minion, " + greeting + "!")

client.run(os.getenv("TOKEN"))
