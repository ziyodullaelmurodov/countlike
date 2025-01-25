from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update
import os 


def start(update: Update, context):
    update.message.reply_text("Salom. Menga rasm yuboring!")

def replyphoto(update: Update, context: CallbackContext):
    ph=update.message.photo[-1].file_id
    update.message.reply_photo(photo=ph)

TOKEN = os.getenv("TOKEN")

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.photo,replyphoto))
dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()