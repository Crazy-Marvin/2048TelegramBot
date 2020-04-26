from configlib import BaseConfig


class Config(BaseConfig):
    token: str
    game_name: str
    game_url: str
    bot_url: str


config = Config.get_instance()
