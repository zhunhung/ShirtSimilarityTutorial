# ShirtSimilarityTutorial - Telegram Bot
Wrapping up your code and serving it to your end users

## Prerequisites

By now, you should have already went through the notebook, deployed and tested your function in Azure Functions. Otherwise, please complete those first:

1. [Code Explanation](https://github.com/zhunhung/ShirtSimilarityTutorial/tree/master/Notebook) - Notebook explaining how it works
2. [Deploying to Azure Functions](https://github.com/zhunhung/ShirtSimilarityTutorial/tree/master/FunctionProject) - Azure Functions setup

### Getting Started

In order to get your own bot, you will have to first create a bot and obtain the token from [BotFather](https://telegram.me/BotFather) in Telegram. Next, insert your function endpoint and bot token into `bot.py`:

```
API_ENDPOINT = "AZURE_FUNCTIONS_ENDPOINT" #<--- Replace with your api endpoint, something like "https://xxx.azurewebsites.net/api/XXX?code=XXXXXXX"
```

and

```
updater = Updater("BOT_TOKEN", use_context=True) #<-- Replace with your token, something like XXXXXXXXX:XXXXXXXXXX
```

### Running the bot

```
python3 bot.py
```
