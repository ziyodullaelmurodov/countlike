from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
import os 
ldl_count = {'like':0,'dislike':0}

def start(update: Update, context):
    update.message.reply_text("Salom. Menga rasm yuboring!")

def replyphoto(update: Update, context: CallbackContext):
    ph=update.message.photo[-1].file_id
    update.message.reply_photo(photo=ph)
    inline_button = InlineKeyboardButton(text="Like👍", callback_data="like")
    inline_button2 = InlineKeyboardButton(text="Dislike👎", callback_data="dislike")
    inline_keyboard = InlineKeyboardMarkup([[inline_button],[inline_button2]])
    update.message.reply_photo(photo=ph, reply_markup=inline_keyboard)
def ilb(update: Update, context: CallbackContext):
    inline_button = InlineKeyboardButton(text="Codewars", url="https://www.codewars.com")    
    inline_keyboard = InlineKeyboardMarkup([[inline_button]])
    update.message.reply_text("Codewarsga o'tish uchun tugmani bosing", reply_markup=inline_keyboard)
def count(update: Update, context: CallbackContext):
    if update.message.text=='like':
        ldl_count['like']+=1
    else:
        ldl_count['dislike']+=1
        
    update.message.reply_text(f"Like: {ldl_count['like']} Dislike: {ldl_count['dislike']}")
TOKEN = os.getenv("TOKEN")

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.photo,replyphoto))
dispatcher.add_handler(CommandHandler('masala',ilb))
dispatcher.add_handler(CommandHandler('ovozlar',count))
dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()