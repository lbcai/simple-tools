import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()



@client.event
async def on_ready():
    ready_message = f'{client.user.name} is here! Type ">help" for a basic command list.'
    channel = discord.utils.get(client.get_all_channels(), name='playfriend')
    await channel.send(ready_message)


@client.event
async def on_message(message):
    print('message received')
    if message.author == client.user:
        return

    help_command_list = '>help: Returns a list of basic commands. \n>test'

    if message.content == '>help':
        await message.channel.send(help_command_list)


client.run(TOKEN)

# Thanks to RealPython.com for tutorials on the basics of Discord bot connection.
