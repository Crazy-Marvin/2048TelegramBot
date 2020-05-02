# Botfather

Start a chat with [@Botfather](https://t.me/botfather) to receive your personal token.
Follow the instructions by him.

Those are the supported [commands](https://core.telegram.org/bots#commands):

```
start - Start
play2048 - Play 2048 😁
help - How to play
about - Info about the bot
source - View the source code
legal - See Terms of Service and Privacy Policy
```

You can inform the Botfather about them for auto-completion but that is optional.

# Installation
To install, unpack this archive in a folder.

 - Install Python 3 on your system and make it available.
 - In a commandline create a virtual environment:
 
```bash
python3 -m venv venv
. venv/bin/activate # in *nix environments
./venv/scripts/activate
pip install -r requirements.txt
```
 - Now create a directory called config, and within create a file called `config.json`. this should leave you with this directory structure:
 
```
 - config
     - config.json
 - gamebot
     - [code files].py
 - venv
     - [some venv files]
 - requirements.txt
 - README.md
 - splash.png
```

![File Structure](https://user-images.githubusercontent.com/15004217/80312097-a859ba00-87e3-11ea-85bf-4cef4d0f1ca3.PNG)

 - The file config.json will need the following content: 
 
```json
{
  "token": "the token provided by the botfather",
  "game_name": "the short name of the game as given in the botfather",
  "game_url": "the http adress of the game html",
  "bot_url": "the ip/hostname of this bot. this is not a webadress, so don't prefix it with http://. it should be in the form of 127.0.0.1 or google.com",
  "healthchecks_url": "a healthchecks.io url or null"
}
```

Here you can see the ```game_name```:

![game_name](https://user-images.githubusercontent.com/15004217/80318150-45c6e500-8808-11ea-966d-162a3f549287.PNG)

# Running
Run the following command
```bash
# in this directory
./venv/bin/python -m gamebot
```
Or on Windows
```
./venv/scripts/python -m gamebot
```

For a persistent setup I would recommend a crontab or a systemd service.

# Monitoring

You can monitor the bot using a service like [Healthchecks.io](https://healthchecks.io/) or [Cronitor](https://cronitor.io/) to get notified when the bot stops working.

![healthchecks](https://user-images.githubusercontent.com/15004217/80873676-887e3680-8cba-11ea-8616-5b189453dbec.PNG)
