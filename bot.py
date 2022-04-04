import telebot

bot = telebot.TeleBot('5227286727:AAGiCZQuk1K2nRgtrVetLws4zXoj4AhAcEY')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Это мой бот!')

bot.polling(non_stop=True)