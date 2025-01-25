from telegram.ext import Updater,CommandHandler
from telegram import Update
import os 


def start(update: Update, context):
    update.message.reply_text("Salom. Menga rasm yuboring!")

TOKEN = os.getenv("TOKEN")

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()