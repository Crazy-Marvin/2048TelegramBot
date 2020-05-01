from threading import Thread
from time import sleep

import requests

from .config import config


def target():
    while True:
        requests.get(config.healthchecks_url)
        sleep(60)


def run():
    if config.healthchecks_url:
        t = Thread(target=target, daemon=True, name="Healthchecks thread")
        t.start()
