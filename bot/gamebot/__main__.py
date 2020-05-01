from .bot import bot
from .server import run as run_server
from .healthcheck import run as run_healthcheck

if __name__ == '__main__':
    run_server()
    run_healthcheck()
    bot.start_polling()
    bot.idle()
