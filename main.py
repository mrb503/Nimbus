import discord
import os


client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

  chat = message.content.lower().split()

  cmd = chat[0]
  city = " ".join(chat[1:])
  
  if message.author == client.user:
    return

  
  if (cmd == '!hello'):
    await message.channel.send("Hi there! I'm Nimbus, your very own weather bot :)")

  elif (cmd == '!hi'):
    await message.channel.send(city)


client.run(os.getenv('TOKEN'))