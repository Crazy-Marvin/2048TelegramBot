from .bot import bot
from .server import run as run_server

if __name__ == '__main__':
    run_server()
    bot.start_polling()
    bot.idle()
