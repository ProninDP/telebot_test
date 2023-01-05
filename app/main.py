#import logging
import sittings
import stablediffusion as stabdiff
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

#logging.basicConfig(
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#    level=logging.INFO
#)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    keyboard = [
        [
            InlineKeyboardButton("help!", callback_data="1"),
            InlineKeyboardButton("generate an image", callback_data="2"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("I'm a Stable Diffusion AI bot! Please choose:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    
    keyboard = [
        [
            InlineKeyboardButton("help!", callback_data="1"),
            InlineKeyboardButton("generate an image", callback_data="2"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=f"Selected option: {query.data}", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    
    keyboard = [
        [
            InlineKeyboardButton("help!", callback_data="1"),
            InlineKeyboardButton("generate an image", callback_data="2"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=f"I'm a bot can generate an image from a text prompt using the stable-diffusion model! Use button generate an image and please enter a massage! Example: an astronaut riding a horse on mars artstation, hd, dramatic lighting, detailed.", reply_markup=reply_markup)

 
async def genimage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    """Echo the user message."""
    #await update.message.reply_text(stabdiff.getimage(update.message.text))
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    
    keyboard = [
        [
            InlineKeyboardButton("help!", callback_data="1"),
            InlineKeyboardButton("generate an image", callback_data="2"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=f"Please enter a massage!", reply_markup=reply_markup)



if __name__ == '__main__':
    application = ApplicationBuilder().token(sittings.TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    #application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CallbackQueryHandler(help_command))
    application.add_handler(CallbackQueryHandler(genimage))
    #application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("help", help_command))
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, genimage))

    #webhook
    application.run_webhook(
    listen=sittings.LOCALHOST_PROXY,
    port=sittings.LOCALPORT_PROXY,
    url_path=sittings.TOKEN,
    webhook_url=sittings.WEBHOOK_URL_BASE + sittings.TOKEN,
)