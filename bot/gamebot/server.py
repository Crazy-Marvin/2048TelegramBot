import traceback
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

from telegram import Bot, Message

from . import bot


class CustomHandler(BaseHTTPRequestHandler):
    # noinspection PyPep8Naming
    def do_GET(self):
        try:
            path = urllib.parse.urlparse(self.path)
            args = urllib.parse.parse_qs(path.query)
            uuid = args.get('uuid')[0]
            score = args.get('score')[0]
            user_id, inline_message_id, message = bot.players.get(uuid)
            message: Message
            chat_id = None if message is None else message.chat_id
            message_id = None if message is None else message.message_id
            tg_bot: Bot = bot.bot.bot
            tg_bot.set_game_score(user_id=user_id, score=score, chat_id=chat_id, message_id=message_id,
                                  inline_message_id=inline_message_id)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes('Success', encoding='utf-8'))
            return
        except:
            traceback.print_exc()


def run():
    server_address = ('0.0.0.0', 8123)
    httpd = HTTPServer(server_address, CustomHandler)
    t = Thread(target=httpd.serve_forever, daemon=True, name="Score thread")
    t.start()
