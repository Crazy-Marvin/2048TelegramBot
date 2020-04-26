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
  "bot_url": "the ip/hostname of this bot. this is not a webadress, so don't prefix it with http://. it should be in the form of 127.0.0.1 or google.com"
}
```

# Running
Run the following command
```bash
# in this directory
./venv/bin/python -m gamebot
```
Or on windows
```
./venv/scripts/python -m gamebot
```

For a persistent setup I would recommend a crontab or a systemd service.
