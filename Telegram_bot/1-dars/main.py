from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

ADMIM_ID = 182534710
token = "6424718517:AAGwWmZxfOLaazS2mMaimZj74CyDaFhsn44"


def start_command(update, context):
    print(update.message.from_user.id)
    print(f'Sizning ismingiz: {update.message.from_user.username}')
    update.message.reply_text(text="Siz /start kamandasini kiritdingiz!")


def show_menu(update, context):
    buttons = [
        [KeyboardButton(text="Kontakt yuborish", request_contact=True),
         KeyboardButton(text="Joylashuv yuborish", request_location=True)],
    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    )


def message_handler(update, context):
    message = update.message.text
    update.message.reply_text(text=f"Sizning xabaringiz '{message}'")


def contact_handler(update, context):
    phone_number = update.message.contact.phone_number
    # update.message.reply_text(text=f"Sizning nomeringiz '{phone_number}'")
    context.bot.send_message(chat_id=ADMIM_ID, text=f"yangi foydalanuvchi raqami: {phone_number}")


def location_handler(update, context):
    location = update.message.location
    # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
    context.bot.send_location(chat_id=ADMIM_ID, latitude=location.latitude, longitude=location.longitude)


def main():
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()