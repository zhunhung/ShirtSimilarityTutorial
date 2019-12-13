import logging
import os
import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Insert your Azure Functions Endpoint
API_ENDPOINT = "AZURE ENDPOINT"
BOT_TOKEN = "BOT_TOKEN"

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Send me an image and I can tell you if you have something similar already.')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def find_similar(update, context):
    """Send a photo of shirt similar to the photo received, only if above certain threshold."""
    logger.info('Find Similar')
    img = update.message.photo[0].get_file()

    # Send POST request to Endpoint
    files = {'file': img.download_as_bytearray()}
    r = requests.post(url=API_ENDPOINT, files=files)

    # Parse response
    response_json = r.json()[0]
    logger.info(response_json)
    result = response_json['result']

    # If similar shirt is found
    if 'score' in response_json.keys():
        update.message.reply_text("Hmm, seems like you have something similar already!")
        img_folder = os.path.join(os.curdir, 'images')
        shirt_fname = os.path.join(img_folder, result.replace('Similar Shirt: ', ''))
        update.message.reply_photo(open(shirt_fname, 'rb'))

    # If no similar shirt is found
    else:
        update.message.reply_text("Ooo, you don't have something similar. But do you really need it though? 🤔")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Insert your TOKEN from BotFather here
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.photo, find_similar))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()