import telebot

bot = telebot.TeleBot('')

@bot.message_handler(content_types='text')
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)