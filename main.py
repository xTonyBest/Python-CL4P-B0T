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
    g = message.content
    if g.lower() == greeting:
      await message.channel.send("Minion, " + greeting.capitalize() + "!")

  if message.content.startswith("/play"):
    url = message.content[6:]
    # TODO: implement a method to play a video given its url



client.run(os.getenv("TOKEN"))
