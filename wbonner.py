import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from folha_mch import scrap

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

title = scrap()

# Command handlers here
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('BOA NOITE, use:\n/news para saber o que tá rolando.\n/enews < i, j > para ver um slice')

def news(update, context) -> None:
    s = ''
    for t in title:
        s += '\n' + t + '\n'
    update.message.reply_text(s)

def enews(update, context) -> None:
    i = int(context.args[0])
    if len(context.args) == 1: j = 0
    else: j = int(context.args[1])
    if i > j:
        update.message.reply_text(title[i])
    elif i == 0 and j == 0:
        update.message.reply_text(title[0])
    else:
        s = ''
        for k in range(i,j):
            s += '\n' + title[k] + '\n'
        update.message.reply_text(s)

def main():
    """Run bot."""
    t = open('./WB_TOKEN')
    token = t.read()
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', start))
    dispatcher.add_handler(CommandHandler('news', news))
    dispatcher.add_handler(CommandHandler('enews', enews))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()