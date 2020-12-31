import os
import random
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot(command_prefix='>')
game_dictionary = {}

class Hangman:
    """Documentation here"""
    from module_vars import hangman_vocab, hangman_list

    def __init__(self):
        self.hangman_image_counter = 0
        self.word = random.choice(self.hangman_vocab)
        self.guess = '```'
        for i in range(0, len(self.word[0])):
            if self.word[0][i] != ' ':
                self.guess += '_ '
            elif self.word[0][i] == ' ':
                self.guess += ' '
            if i == len(self.word[0]) - 1:
                self.guess += '```'

    async def hangman_output(self, message):
        await message.channel.send(self.hangman_list[self.hangman_image_counter])
        await message.channel.send(self.guess)

    @bot.command(name='hm', help='Place a single letter after "hm" to make a guess.', pass_context=True)
    async def hangman_check(self, ctx):
        for letter in self.word[0]:
            if ctx.message[-1] == letter:
                print(self.word[0].index(letter))


@bot.command(name='hmstart', help='Starts a game of hangman.')
async def hangman_start(message):
    game_dictionary[message.author] = Hangman()
    await Hangman.hangman_output(game_dictionary[message.author], message)

#bot.add_cog(Hangman())


@bot.event
async def on_ready():
    ready_message = f'{bot.user.name} is here! Type ">help" for a basic command list.'
    channel = discord.utils.get(bot.get_all_channels(), name='playfriend')
    await channel.send(ready_message)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

bot.run(TOKEN)
