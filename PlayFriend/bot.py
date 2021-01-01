import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot(command_prefix='>')
game_dictionary = {}


class Hangman(commands.Cog):
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

    async def hangman_wrong(self, ctx):
        game_dictionary[ctx.message.channel].hangman_image_counter += 1
        await Hangman.hangman_output(game_dictionary[ctx.message.channel], ctx.message)
        if game_dictionary[ctx.message.channel].hangman_image_counter == 6:
            bot_message = f'Your man is hung. RIP. The word was {game_dictionary[ctx.message.channel].word[0].lower()}, ' \
                          f'which means {game_dictionary[ctx.message.channel].word[1].lower()}.'
            game_dictionary[ctx.message.channel] = None
            await Hangman.hangman_output(game_dictionary[ctx.message.channel], ctx.message)
            await ctx.message.channel.send(bot_message)

    async def hangman_win(self, ctx):
        bot_message = f'Congratulations! You won. The word was {game_dictionary[ctx.message.channel].word[0].lower()}, ' \
                      f'which means {game_dictionary[ctx.message.channel].word[1].lower()}.'
        game_dictionary[ctx.message.channel] = None
        await ctx.message.channel.send(bot_message)

    @commands.command(name='hm', help='Make a guess. Use single letters unless you are confident you know the entire word!')
    async def hangman_check(self, ctx, message):
        print(game_dictionary[ctx.message.channel].word[0])
        if len(message.strip()) == 1:
            hm_letter_counter = 0
            for letter in range(0, len(game_dictionary[ctx.message.channel].word[0])):
                if message[-1].lower() == game_dictionary[ctx.message.channel].word[0][letter].lower():
                    hm_letter_counter += 1
                    # replace the '_' corresponding to letter with message[-1].upper()
                    # even indices = '_' and odd = spaces that must be preserved.
                    # change guess to a list with _ for each letter, go through list to change and go off list to print
                    game_dictionary[ctx.message.channel].guess
                    [letter*2]
                else:
                    pass
            if hm_letter_counter == 0:
                await Hangman.hangman_wrong(game_dictionary[ctx.message.channel], ctx)
            else:
                await Hangman.hangman_output(game_dictionary[ctx.message.channel], ctx.message)
        else:
            if game_dictionary[ctx.message.channel].word[0].lower() == message.strip().lower():
                await Hangman.hangman_win(game_dictionary[ctx.message.channel], ctx)
            else:
                await Hangman.hangman_wrong(game_dictionary[ctx.message.channel], ctx)



@bot.command(name='hmstart', help='Starts a game of hangman.')
async def hangman_start(message):
    if message.channel not in game_dictionary or game_dictionary[message.channel] is None:
        game_dictionary[message.channel] = Hangman()
        await Hangman.hangman_output(game_dictionary[message.channel], message)
    else:
        await message.channel.send('There is already a hangman game in this channel!')

bot.add_cog(Hangman())


@bot.event
async def on_ready():
    ready_message = f'{bot.user.name} is here! Type ">help" for a basic command list.'
    channel = discord.utils.get(bot.get_all_channels(), name='playfriend')
    await channel.send(ready_message)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'hi':
        await message.channel.send('<:rip:280861016911380480>')

    await bot.process_commands(message)

bot.run(TOKEN)
