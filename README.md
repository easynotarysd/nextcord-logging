Nextcord Logging
===================



Notices:
-------
* This module was based off of [discord-logging](https://pypi.org/project/discord-logging/ "discord-logging PyPi page") by [grarich](https://pypi.org/user/grarch/ "grarich PyPi profile").

Installation:
-------------

###### Install with pip:
```
pip install nextcord-logging
```
###### Usage
```python
import logging
from nextcord.ext import commands
from nextcord_logging import Discord_Handler

logger = logging.getLogger()

WEBHOOK_URL = "Your webhook url"
handler = Discord_Handler(WEBHOOK_URL)

logger.addHandler(handler)

bot = commands.Bot(command_prefix="!")

bot.run("token")
```
###### Update with pip:
```
pip install nextcord-logging --upgrade
```

###### Install from source:
```
python setup.py install
```

Links:
------
* [GitHub repo](https://github.com/AvocadoManYT/nextcord-logging)
* [PyPi project page](https://pypi.org/project/nextcord-logging/)