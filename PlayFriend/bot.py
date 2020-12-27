import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

hangman_full = (f'```\n________\n'
                    f'|/    _|_\n'
                    r"|    |x x|"
                    f'\n'
                    r'|    /[Y]\ '
                    f'\n'
                    r'|     / \ '
                    f'\n'
                    f'|_____```')

hangman1 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|      '
            f'\n'
            r'|      '
            f'\n'
            f'|_____```')

hangman2 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|     [Y] '
            f'\n'
            r'|       '
            f'\n'
            f'|_____```')

hangman3 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|    /[Y] '
            f'\n'
            r'|       '
            f'\n'
            f'|_____```')

hangman4 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|    /[Y]\ '
            f'\n'
            r'|       '
            f'\n'
            f'|_____```')

hangman5 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|    /[Y]\ '
            f'\n'
            r'|     /'
            f'\n'
            f'|_____```')


@client.event
async def on_ready():
    ready_message = f'{client.user.name} is here! Type ">help" for a basic command list.'
    channel = discord.utils.get(client.get_all_channels(), name='playfriend')
    await channel.send(ready_message)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    help_command_list = '>help: Returns a list of basic commands. \n>hangman: Start a game of hangman.'

    if message.content.lower() == '>help':
        await message.channel.send(help_command_list)

    if message.content.lower() == '>hangman':
        await message.channel.send(hangman_full)
        await message.channel.send(hangman1)
        await message.channel.send(hangman2)
        await message.channel.send(hangman3)
        await message.channel.send(hangman4)
        await message.channel.send(hangman5)


client.run(TOKEN)

# Thanks to RealPython.com for tutorials on the basics of Discord bot connection.
