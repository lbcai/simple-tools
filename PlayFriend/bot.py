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
    """Allows users to play hangman. Use function hangman_start to create game instances.
    Function hangman_custom allows a user to submit their own word and restarts the game with that word as self.word[0].
    Function hangman_check is used to check if the user's guess of a single letter or a full word matches self.word[0].
    Function hangman_wrong is used when a guess is incorrect. It adds a hangman body part to the gallows, and when
        the man is complete, it causes the user to lose the game.
    Function hangman_win is used when the user has successfully guessed the entire word and won the game.
    Function hangman_output uses hangman_guess_filler to display the current state of the word and the man in chat."""

    from module_vars import hangman_vocab, hangman_list

    def __init__(self):
        self.hangman_image_counter = 0
        self.word = random.choice(self.hangman_vocab)
        Hangman.hangman_guess_list(self)

    def hangman_guess_list(self):
        self.guess_list = []
        for i in range(0, len(self.word[0])):
            self.guess_list.append('_')
        Hangman.hangman_guess_filler(self)

    def hangman_guess_filler(self):
        self.guess = '```'
        for item in self.guess_list:
            self.guess += item
            if item != ' ':
                self.guess += ' '
        self.guess += '```'

    @commands.command(name='hmword', help='Submit a custom word in spoiler tags, ex. ||word||. This will restart the game.')
    async def hangman_custom(self, ctx, message):
        await ctx.channel.send(f'A new game with {ctx.message.author.mention}\'s custom word is starting.')
        hangman_custom_word = ''
        if '||' in message.strip():
            for item in message.strip():
                if item == '|':
                    pass
                else:
                    hangman_custom_word += item
            await ctx.message.delete()
            if ctx.message.channel in game_dictionary:
                game_dictionary[ctx.message.channel].hangman_image_counter = 0
                game_dictionary[ctx.message.channel].word = (hangman_custom_word, '...google it')
                Hangman.hangman_guess_list(game_dictionary[ctx.message.channel])
            await Hangman.hangman_output(game_dictionary[ctx.message.channel], ctx.message)
        else:
            pass

    async def hangman_output(self, message):
        Hangman.hangman_guess_filler(self)
        await message.channel.send(self.hangman_list[self.hangman_image_counter])
        await message.channel.send(self.guess)

    async def hangman_wrong(self, ctx):
        game_dictionary[ctx.message.channel].hangman_image_counter += 1
        await Hangman.hangman_output(game_dictionary[ctx.message.channel], ctx.message)
        if game_dictionary[ctx.message.channel].hangman_image_counter == 6:
            bot_message = f'Your man is hung. RIP. The word was {game_dictionary[ctx.message.channel].word[0].lower()}, ' \
                          f'which means {game_dictionary[ctx.message.channel].word[1]}.'
            await ctx.message.channel.send(bot_message)
            game_dictionary.pop(ctx.message.channel, None)

    async def hangman_win(self, ctx):
        bot_message = f'Congratulations! You won. The word was {game_dictionary[ctx.message.channel].word[0].lower()}, ' \
                      f'which means {game_dictionary[ctx.message.channel].word[1]}.'
        await ctx.message.channel.send(bot_message)
        game_dictionary.pop(ctx.message.channel, None)

    @commands.command(name='hm', help='Make a guess. Use single letters unless you are confident you know the entire word!')
    async def hangman_check(self, ctx, message):
        if message.isalpha() is False:
            await ctx.message.channel.send('Use a letter.')
        else:
            if len(message.strip()) == 1:
                hm_letter_counter = 0
                for letter in range(0, len(game_dictionary[ctx.message.channel].word[0])):
                    if message[-1].strip().lower() == game_dictionary[ctx.message.channel].word[0][letter].lower():
                        hm_letter_counter += 1
                        game_dictionary[ctx.message.channel].guess_list[letter] = game_dictionary[ctx.message.channel].word[0][letter].upper()
                    else:
                        pass
                if hm_letter_counter == 0:
                    await Hangman.hangman_wrong(game_dictionary[ctx.message.channel], ctx)
                else:
                    await Hangman.hangman_output(game_dictionary[ctx.message.channel], ctx.message)
            else:
                if game_dictionary[ctx.message.channel].word[0].lower() == message.strip().lower():
                    for letter in range(0, len(game_dictionary[ctx.message.channel].word[0])):
                        game_dictionary[ctx.message.channel].guess_list[letter] = game_dictionary[ctx.message.channel].word[0][letter].upper()
                    await Hangman.hangman_output(game_dictionary[ctx.message.channel], ctx.message)
                    await Hangman.hangman_win(game_dictionary[ctx.message.channel], ctx)
                else:
                    await Hangman.hangman_wrong(game_dictionary[ctx.message.channel], ctx)
            if '_' not in game_dictionary[ctx.message.channel].guess_list:
                await Hangman.hangman_win(game_dictionary[ctx.message.channel], ctx)

    @commands.command(name='hmquit', help='Quit the current hangman game.')
    async def hangman_quit(self, ctx):
        game_dictionary.pop(ctx.message.channel, None)
        await ctx.message.channel.send('The hangman game has ended.')



@bot.command(name='hmstart', help='Starts a game of hangman.')
async def hangman_start(message):
    if message.channel not in game_dictionary:
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
