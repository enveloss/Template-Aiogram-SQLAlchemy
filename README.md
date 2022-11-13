# Telegram-bot template with Aiogram & SQLAlchemy

### Quickly start:
#### You need to create ```.env``` file in ```./settings``` folder and add there these values:

```
BOT_TOKEN=
CONN_STRING=mysql+aiomysql://{username}:{password}@{host}:{port}/{database}

```

#### Also you need to replace ```username``` and *others* values in the ```CONN_STRING```

### That`s It! Run this commands in the root directory 

```console
$ > pip3 install -r requirements.txt
$ > app.py
```

### There are also Others Opportunities here: 
- APScheduler
- Logger
- JSONConfig -> [docs here](https://github.com/enveloss/py_json_config)
- Made Middlewares 
- Simple admin-section (you need to setting it)