# Work with Python 3.6
import random

from discord import Game
from discord.ext.commands import Bot

TOKEN = 'NDk2MzE3NTQwMTQyNjc4MDE2.DpPkVw.CIIy-G3g40c9sKJgIsCWX2oP7kE'
BOT_PREFIX = ("?", "!")
bot = Bot(command_prefix=BOT_PREFIX)


@bot.command(descripton="Api key zur Serverwahl eingeben",
             brief="Api key zur Serverwahl eingeben",
             pass_context=True)
async def reg(ctx):
    msg = "Einfach den API Key mir schicken und " \
          "dann wirst du zugeorndet! Bitte warten :P"
    await bot.send_message(ctx.message.author, msg)


@bot.command(brief="Rate mal was passiert du Pleb!",
             pass_context=True)
async def beleidigeMich(context):
    possible_brainfarts = ["Du Stinkst", "Geh dich Erhängen",
                           "Deine Mudda sammelt hässliche Kinder!",
                           "Ich kann schneller Radfahren als du!"]
    await bot.say(random.choice(
        possible_brainfarts) + ", " + context.message.author.mention)


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="Warten auf Anweisungen,Master!"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


bot.run(TOKEN)
