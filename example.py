#!/usr/bin/env python3

import os
import logging
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

API_KEY=os.environ['TELEGRAM_BOT_TOKEN']
updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update: Update, context: CallbackContext):
    input=str(update.message.text)
    output=input.split(' ',1)[1]
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)

echo_handler = CommandHandler('echo', echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
