from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ParseMode #PARSEMODE IS FOR HTML RESPONSE TYPE IF WE NEED

#BASIC LOGGING FUNCTION
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN ='INSERT YOUR BOT TOKEN HERE'

#BOT CONFIGURATION
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
#CONFIGURATION END

#COMMAND FUNCTIONS
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='START MESSAGE TO SEND')

#BOT FUNCTIONS
def TextFunction(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='MESSAGE TO SEND HERE')

def ImgFunction(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='MESSAGE TO SEND HERE')
    #IF WE WANT TO SEND A PHOTO THE PATTERN IS:
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo='PHOTO URL', caption= 'CAPTION BELOW THE PHOTO TO SEND')

#HANDLER FOR TEXT MESSAGES ONLY
TextHandler =  MessageHandler(Filters.text,TextFunction)
#HANDLER FOR IMAGE MESSAGE ONLY
photoHandler =  MessageHandler(Filters.photo, ImgFunction)

#YOU CAN COMBINE 2 OR MORE FILETRS. EXAMPLE AN HANDLER TO MANAGE MESSAGES WITH CAPTION WILL BE:
# GotImageAndCaption = MessageHandler(Filters.photo & Filters.caption, some_function)

#HANDLER FOR COMMAND
start_handler = CommandHandler('start', start)

#ADDING HANDLER AS EVENT LISTENER
dispatcher.add_handler(TextHandler)
dispatcher.add_handler(start_handler)    

#UPDATER START LOOPING
updater.start_polling()

