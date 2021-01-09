import os
import random
import discord
import emojis
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot(command_prefix='>')
hm_game_dictionary = {}
ttt_game_dictionary = {}

#currently working on setting up backend for databasing and allowing bot to stay online indefinitely
#must set up databasing to save long games of dungeon, also must account for large numbers of items, mobs, special events
#consider storing a lot of these things in module_vars.py
#possibly need multiple classes for dungeon game class.


class Dungeon(commands.Cog):
    """Docs here"""
    print('placeholder')


class Tictactoe(commands.Cog):
    """Docs here"""
    #plan algo for winning ttt games

    def __init__(self):
        self.tt_board_list = [':white_medium_square:' for _ in range(0, 9)]

    @commands.command(name='ttsetup', help='Customize the marker you place on the board.')
    async def ttt_game_setup(self, ctx):

        def ttt_get_emoji(emoji_response):
            return ctx.message.channel == emoji_response.channel and ctx.message.author in \
                   ttt_game_dictionary[ctx.message.channel][1:2] and \
                   emojis.count(emoji_response.content.lower().strip()) > 0

        await ctx.message.channel.send('Put a default emoji into the chat. The marker you use on the board will change.')

        symbol = await bot.wait_for('message', check=ttt_get_emoji)
        symbol = emojis.decode(random.choice(list(emojis.get(symbol.content))))
        if ctx.message.author == ttt_game_dictionary[ctx.message.channel][1]:
            ttt_game_dictionary[ctx.message.channel][3] = symbol
        elif ctx.message.author == ttt_game_dictionary[ctx.message.channel][2]:
            ttt_game_dictionary[ctx.message.channel][4] = symbol

    @commands.command(name='ttquit', help='Quit the current tic tac toe game.')
    async def ttt_quit(self, ctx):
        ttt_game_dictionary[ctx.message.channel][0] = None
        await ctx.message.channel.send('The tic tac toe game has ended.')

    async def ttt_output(self, ctx):
        tt_board = '{0}{1}{2} \n{3}{4}{5} \n{6}{7}{8}'.format(*ttt_game_dictionary[ctx.message.channel][0].tt_board_list)
        await ctx.message.channel.send(tt_board)

    @commands.command(name='tt', help="Use the command >tthelp if it's your first time playing.")
    async def ttt_mark_square(self, ctx, message):
        print('placeholder')
        await ctx.message.channel.send('hi')

    @commands.command(name='tthelp', help='Sends a message explaining how to play.')
    async def ttt_mark_square(self, ctx):
        await ctx.message.channel.send('To mark a square, type >tt # according to this chart!\n'
                                       ':one::two::three: \n:four::five::six: \n:seven::eight::nine:')


@bot.command(name='ttstart', help='Starts a game of tic tac toe.')
async def ttt_start(message):

    def ttt_get_players(num_response):
        # Check to make sure the game starter is answering the question.
        return message.author == num_response.author and message.channel == num_response.channel and \
               num_response.content.lower().strip() in ['1', '2', 'one', 'two', '1p', '2p']

    def ttt_get_second_player(num_response):
        return message.channel == num_response.channel and \
               num_response.content.lower().strip() in ['me', 'i']

    if message.channel not in ttt_game_dictionary or ttt_game_dictionary[message.channel][0] is None:
        ttt_players = 0
        ttt_player_one = 0
        ttt_player_two = 0
        await message.channel.send('1p and 2p games are allowed. How many players are there?')
        while ttt_players == 0:
            response = await bot.wait_for('message', check=ttt_get_players)
            if response.content.lower().strip() in ['1', 'one', '1p']:
                ttt_player_one = response.author
                ttt_player_two = f'{bot.user.name}'
                ttt_players = 1
            elif response.content.lower().strip() in ['2', 'two', '2p']:
                ttt_player_one = response.author
                await message.channel.send('Who is the second player? Type "me".')
                ttt_player_two = 0
                while ttt_player_two == 0:
                    second_response = await bot.wait_for('message', check=ttt_get_second_player)
                    ttt_player_two = second_response.author
                ttt_players = 2
            else:
                await message.channel.send('Please specify whether there are one or two players.')

            if message.channel not in ttt_game_dictionary:
                ttt_game_dictionary[message.channel] = [Tictactoe(), ttt_player_one, ttt_player_two, ':x:', ':o:']
            else:
                ttt_game_dictionary[message.channel][0] = Tictactoe()

            if random.choice([0, 1]) == 1:
                ttt_game_dictionary[message.channel][3:4] = ttt_game_dictionary[message.channel][4:3]
                ttt_game_dictionary[message.channel][1:2] = ttt_game_dictionary[message.channel][2:1]
                if ttt_game_dictionary[message.channel][1] is not f'{bot.user.name}':
                    await message.channel.send(f'{ttt_game_dictionary[message.channel][1].mention} is going first.')
                else:
                    await message.channel.send('I am going first.')
            else:
                await message.channel.send(f'{ttt_game_dictionary[message.channel][1].mention} is going first.')

            await Tictactoe.ttt_output(ttt_game_dictionary[message.channel], message)
    else:
        await message.channel.send('There is already a tic tac toe game in this channel!')


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
            if ctx.message.channel in hm_game_dictionary:
                hm_game_dictionary[ctx.message.channel].hangman_image_counter = 0
                hm_game_dictionary[ctx.message.channel].word = (hangman_custom_word, '...google it')
                Hangman.hangman_guess_list(hm_game_dictionary[ctx.message.channel])
            await Hangman.hangman_output(hm_game_dictionary[ctx.message.channel], ctx.message)
        else:
            pass

    async def hangman_output(self, message):
        Hangman.hangman_guess_filler(self)
        await message.channel.send(self.hangman_list[self.hangman_image_counter])
        await message.channel.send(self.guess)

    async def hangman_wrong(self, ctx):
        hm_game_dictionary[ctx.message.channel].hangman_image_counter += 1
        await Hangman.hangman_output(hm_game_dictionary[ctx.message.channel], ctx.message)
        if hm_game_dictionary[ctx.message.channel].hangman_image_counter == 6:
            bot_message = f'Your man is hung. RIP. The word was {hm_game_dictionary[ctx.message.channel].word[0].lower()}, ' \
                          f'which means {hm_game_dictionary[ctx.message.channel].word[1]}.'
            await ctx.message.channel.send(bot_message)
            hm_game_dictionary.pop(ctx.message.channel, None)

    async def hangman_win(self, ctx):
        bot_message = f'Congratulations! You won. The word was {hm_game_dictionary[ctx.message.channel].word[0].lower()}, ' \
                      f'which means {hm_game_dictionary[ctx.message.channel].word[1]}.'
        await ctx.message.channel.send(bot_message)
        hm_game_dictionary.pop(ctx.message.channel, None)

    @commands.command(name='hm', help='Make a guess. Use single letters unless you are confident you know the entire word!')
    async def hangman_check(self, ctx, message):
        if message.isalpha() is False:
            await ctx.message.channel.send('Use a letter.')
        else:
            if len(message.strip()) == 1:
                hm_letter_counter = 0
                for letter in range(0, len(hm_game_dictionary[ctx.message.channel].word[0])):
                    if message[-1].strip().lower() == hm_game_dictionary[ctx.message.channel].word[0][letter].lower():
                        hm_letter_counter += 1
                        hm_game_dictionary[ctx.message.channel].guess_list[letter] = hm_game_dictionary[ctx.message.channel].word[0][letter].upper()
                    else:
                        pass
                if hm_letter_counter == 0:
                    await Hangman.hangman_wrong(hm_game_dictionary[ctx.message.channel], ctx)
                else:
                    await Hangman.hangman_output(hm_game_dictionary[ctx.message.channel], ctx.message)
            else:
                if hm_game_dictionary[ctx.message.channel].word[0].lower() == message.strip().lower():
                    for letter in range(0, len(hm_game_dictionary[ctx.message.channel].word[0])):
                        hm_game_dictionary[ctx.message.channel].guess_list[letter] = hm_game_dictionary[ctx.message.channel].word[0][letter].upper()
                    await Hangman.hangman_output(hm_game_dictionary[ctx.message.channel], ctx.message)
                    await Hangman.hangman_win(hm_game_dictionary[ctx.message.channel], ctx)
                else:
                    await Hangman.hangman_wrong(hm_game_dictionary[ctx.message.channel], ctx)
            if '_' not in hm_game_dictionary[ctx.message.channel].guess_list:
                await Hangman.hangman_win(hm_game_dictionary[ctx.message.channel], ctx)

    @commands.command(name='hmquit', help='Quit the current hangman game.')
    async def hangman_quit(self, ctx):
        hm_game_dictionary.pop(ctx.message.channel, None)
        await ctx.message.channel.send('The hangman game has ended.')


@bot.command(name='hmstart', help='Starts a game of hangman.')
async def hangman_start(message):
    if message.channel not in hm_game_dictionary:
        hm_game_dictionary[message.channel] = Hangman()
        await Hangman.hangman_output(hm_game_dictionary[message.channel], message)
    else:
        await message.channel.send('There is already a hangman game in this channel!')

bot.add_cog(Hangman())
bot.add_cog(Tictactoe())


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
