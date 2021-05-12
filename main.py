import discord
import os
import weather


client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='the clouds'))
  print("We have logged in as {0.user}".format(client))
  

@client.event
async def on_message(message):

  chat = message.content.lower().split()

  cmd = chat[0]
  city = " ".join(chat[1:])
  data = weather.getData(city)
  
  if message.author == client.user:
    return

  
  if (cmd == '!hello'):
    await message.channel.send("Hi there! I'm Nimbus, your very own weather bot :)")

  elif (cmd == '!commands'):
    await message.channel.send("Here's what I can do: \n!temp - get the current temperature \n!current - get the current conditions")
  
  elif (cmd == '!temp'):
    temp = weather.getTemperature(data)
    await message.channel.send("🌡 {:.2f}".format(temp) + " °F")

  elif (cmd == '!current'):
    basic = weather.getCurrentBasic(data)
    descr = weather.getCurrentDescr(data)
    if basic == 'Rain':
      icon = '☔ '
    elif basic == 'Drizzle':
      icon = '🌧 '
    elif basic == 'Mist':
      icon = '🌫 '
    elif basic == 'Clouds':
      icon = '☁️ '
    elif basic == 'Clear':
      icon = '☀️ ' 
    elif basic == 'Snow':
      icon = '❄️ '
    elif basic == 'Thunderstorm':
      icon = '⛈ '
    else:
      icon = ' '
    
    await message.channel.send(icon + "It's currently " + descr + "!")

client.run(os.getenv('TOKEN'))