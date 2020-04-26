import random
import string
import urllib.parse
from functools import partial

from telegram import Update, InlineQuery, InlineQueryResultGame, CallbackQuery, ParseMode
from telegram.ext import Updater, CallbackContext, Dispatcher, CommandHandler, InlineQueryHandler, CallbackQueryHandler

from .config import config

bot = Updater(token=config.token, use_context=True)
dis: Dispatcher = bot.dispatcher


def generate_uuid():
    g = lambda: ''.join(random.choice(string.hexdigits) for _ in range(32))
    i = g()
    while i in players:
        i = g()
    return i


players = dict()


def command(name):
    return partial(CommandHandler, name)


@command('start')
def start_handler(update: Update, ctx: CallbackContext):
    ctx.bot.send_message(chat_id=update.effective_chat.id,
                         text="This bot allows you to play 2048, right here in Telegram. Try it out using /play2048")


@command('play2048')
def play_handler(update: Update, ctx: CallbackContext):
    ctx.bot.send_game(chat_id=update.effective_chat.id,
                      game_short_name=config.game_name)


@command('about')
def about_handler(update: Update, ctx: CallbackContext):
    ctx.bot.send_message(chat_id=update.effective_chat.id,
                         text="This bot is based on the game [2048](https://github.com/gabrielecirulli/2048) by"
                              " [Gabriele Cirulli](https://gabrielecirulli.com/).\n"
                              "You can find the source [here](https://github.com/Crazy-Marvin/2048TelegramBot).\n"
                              "Please feel welcome to join the [Telegram group](https://t.me/CrazyMarvin) "
                              "and [Slack](https://slack.crazymarvin.com/).", parse_mode=ParseMode.MARKDOWN)


@command('legal')
def legal_handler(update: Update, ctx: CallbackContext):
    ctx.bot.send_message(chat_id=update.effective_chat.id,
                         text="You can find our legal documents at https://poopjournal.rocks/2048/legal/2048_legal.pdf")


@command('source')
def source_handler(update: Update, ctx: CallbackContext):
    ctx.bot.send_message(chat_id=update.effective_chat.id,
                         text="You can find the source code for this bot at: "
                              "https://github.com/Crazy-Marvin/2048TelegramBot")


@command('help')
def help_handler(update: Update, ctx: CallbackContext):
    ctx.bot.send_message(chat_id=update.effective_chat.id,
                         text="**How to play:** Use your arrow keys to move the tiles. When two tiles with the same"
                              " number touch, they merge into one! Join the numbers and get the *2048* tile!",
                         parse_mode=ParseMode.MARKDOWN)


@InlineQueryHandler
def inline_handler(update: Update, ctx: CallbackContext):
    query: InlineQuery = update.inline_query
    ctx.bot.answer_inline_query(inline_query_id=query.id,
                                results=[InlineQueryResultGame(id='play2048', game_short_name=config.game_name)])


def get_score_url(uuid):
    return "http://" + config.bot_url + ":8123/report?uuid=" + uuid + "&score="


@CallbackQueryHandler
def callback_handler(update: Update, ctx: CallbackContext):
    query: CallbackQuery = update.callback_query
    if query.game_short_name == config.game_name:
        uuid = generate_uuid()
        players[uuid] = (update.effective_user.id, query.inline_message_id, query.message)
        query.answer(url=config.game_url + "?p=" + urllib.parse.quote_plus(get_score_url(uuid)))


dis.add_handler(callback_handler)
dis.add_handler(legal_handler)
dis.add_handler(start_handler)
dis.add_handler(about_handler)
dis.add_handler(help_handler)
dis.add_handler(play_handler)
dis.add_handler(source_handler)
dis.add_handler(inline_handler)
