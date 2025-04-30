import telebot

bot = telebot.TeleBot("7613297110:AAHJhcUaEiixGA8W1zNqrhLG_Lz7wc5SKbc")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я работаю.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
