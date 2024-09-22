from telebot import TeleBot
from keys import generate_main_menu, laptop_manu, buy_laptop
from data_base import data
from parsing import image

token = '6727255306:AAGegLEDMmh9aIPzGNPBc7RyuadEI_AVA5Y'
bot = TeleBot(token)


@bot.message_handler(['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    send_mess = f'Salom!\nIsmingiz: {first_name}\nFamiliyangiz{last_name}\nSizning user ID: {user_id}'
    contact = bot.send_message(chat_id, send_mess, reply_markup=generate_main_menu())
    bot.register_next_step_handler(contact, registeration)


def registeration(message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    bot.send_message(chat_id, f"Siz {phone_number} nomer orqali ro'yxatdan o'tdingiz!", reply_markup=laptop_manu())
    bot.register_next_step_handler(message, laptop)
    print(phone_number)


def laptop(message):
    chat_id = message.chat.id
    if message.text == 'Laptop':
        for x in data:
            lap_n = x[0]
            lap_p = x[2]
            lap_c = x[3]
            laptop_data = (f"noutbuk nomi : {lap_n}\n\n narxi: {lap_p} \n\n oyiga:{lap_c}")
            bot.send_photo(chat_id, image, caption=laptop_data, reply_markup=buy_laptop())


while True:
    try:
        print("Bot run!")
        bot.polling()

    except:
        print("error")
        bot.stop_polling()






